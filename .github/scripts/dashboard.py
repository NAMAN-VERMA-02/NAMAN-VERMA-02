"""Render assets/dashboard.svg from live GitHub data. Run daily by the recent-activity workflow."""
import datetime as dt, html, json, os, urllib.request

USER = "NAMAN-VERMA-02"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
FLAGSHIPS = ["capproof", "agentreplay", "mcpfuzz"]


def api(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Accept": "application/vnd.github+json",
                                          **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    return json.load(urllib.request.urlopen(req, timeout=30))


repos = [r for r in api(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")
         if not r["fork"] and r["name"] != USER]

Q = ('{user(login:"%s"){contributionsCollection{totalCommitContributions '
     'contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}' % USER)
cal = api("https://api.github.com/graphql", {"query": Q})
assert "data" in cal, cal
cc = cal["data"]["user"]["contributionsCollection"]
days = [d for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
total = cc["contributionCalendar"]["totalContributions"]
commits = cc["totalCommitContributions"]

# streaks: today may still be empty, so the current streak may end yesterday
longest = run = 0
for d in days:
    run = run + 1 if d["contributionCount"] else 0
    longest = max(longest, run)
cur, i = 0, len(days) - 1
if days and not days[i]["contributionCount"]:
    i -= 1
while i >= 0 and days[i]["contributionCount"]:
    cur, i = cur + 1, i - 1

# PRs merged into other people's repos by someone other than me (a maintainer said yes)
found = api(f"https://api.github.com/search/issues?q=author:{USER}+is:pr+is:merged+-user:{USER}&per_page=50")["items"]
merged = 0
for it in found:
    pr = api(it["pull_request"]["url"])
    if (pr.get("merged_by") or {}).get("login") != USER:
        merged += 1

ci_ok = 0
for name in FLAGSHIPS:
    runs = api(f"https://api.github.com/repos/{USER}/{name}/actions/workflows/ci.yml/runs?branch=main&per_page=1")["workflow_runs"]
    ci_ok += bool(runs) and runs[0]["conclusion"] == "success"

langs = {}
for r in repos:
    for k, v in api(r["languages_url"]).items():
        langs[k] = langs.get(k, 0) + v
skip = {"HTML", "CSS", "Dockerfile", "Shell", "Batchfile", "PowerShell", "Makefile"}
code = {k: v for k, v in langs.items() if k not in skip}
top = sorted(code.items(), key=lambda kv: -kv[1])[:5]
tot = sum(code.values()) or 1

assert repos and days, "GitHub returned no data; refusing to overwrite the dashboard"

# ---------- render ----------
e = html.escape
COL = ["#e6edf3", "#a5b4c3", "#7d8a98", "#5b6672", "#3d454f"]
o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="1200" height="560" role="img" '
     f'aria-label="GitHub metrics for {USER}">',
     '<style>.m{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.s{font-family:"Segoe UI",Inter,Arial,sans-serif}'
     '.h{fill:#e6edf3;font-size:15px;font-weight:700;letter-spacing:2px}.k{fill:#8b949e;font-size:15px}'
     '.v{fill:#e6edf3;font-size:15px;font-weight:700}.big{fill:#fff;font-size:56px;font-weight:700}'
     '.lab{fill:#e6edf3;font-size:20px}.sub{fill:#6e7681;font-size:15px}'
     '.f{opacity:0;animation:f .6s ease-out forwards}@keyframes f{to{opacity:1}}'
     '.ring{stroke-dasharray:440;stroke-dashoffset:440;animation:r 1.6s ease-out .4s forwards}@keyframes r{to{stroke-dashoffset:0}}'
     '.bar{transform-box:fill-box;transform:scaleX(0);animation:b 1s ease-out forwards}@keyframes b{to{transform:scaleX(1)}}</style>',
     '<defs><pattern id="g" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#fff" stroke-opacity=".04"/></pattern></defs>']


def panel(x, y, w, h):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#05070a" stroke="#21262d"/>'
             f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="url(#g)"/>')


# panel 1: metrics
panel(0, 0, 590, 250)
o.append('<text x="28" y="44" class="s h"><tspan fill="#f0883e">⚡</tspan> ACTIVITY &amp; METRICS</text>')
rows = [("Public repositories", str(len(repos))),
        ("Contributions, last 12 months", f"{total:,}"),
        ("Commits, last 12 months", f"{commits:,}"),
        ("PRs merged by other maintainers", str(merged)),
        ("Flagship CI passing on main", f"{ci_ok}/{len(FLAGSHIPS)}")]
for i, (k, v) in enumerate(rows):
    y = 88 + i * 34
    o.append(f'<g class="f" style="animation-delay:{.1 + i * .12:.2f}s">'
             f'<circle cx="38" cy="{y - 5}" r="9" fill="#0d1117" stroke="#30363d"/><circle cx="38" cy="{y - 5}" r="3" fill="#e6edf3"/>'
             f'<text x="58" y="{y}" class="s k">{e(k)}</text><text x="562" y="{y}" class="m v" text-anchor="end">{e(v)}</text></g>')

# panel 2: languages
panel(610, 0, 590, 250)
o.append('<text x="638" y="44" class="s h"><tspan fill="#58a6ff">▮</tspan> TOP LANGUAGES <tspan fill="#6e7681" font-size="12">BY BYTES OF CODE</tspan></text>')
x = 638
for i, (k, v) in enumerate(top):
    w = max(6, 534 * v / tot - 4)
    o.append(f'<rect class="bar" style="animation-delay:{.2 + i * .1:.1f}s" x="{x:.1f}" y="62" width="{w:.1f}" height="8" rx="4" fill="{COL[i]}"/>')
    x += w + 4
for i, (k, v) in enumerate(top):
    y = 104 + i * 29
    o.append(f'<g class="f" style="animation-delay:{.3 + i * .1:.1f}s"><circle cx="644" cy="{y - 5}" r="5" fill="{COL[i]}"/>'
             f'<text x="660" y="{y}" class="s v">{e(k)}</text>'
             f'<text x="1172" y="{y}" class="m k" text-anchor="end">{100 * v / tot:.1f}%</text></g>')

# panel 3: streaks
panel(0, 270, 1200, 290)
o += [f'<text x="200" y="400" class="s big" text-anchor="middle">{total:,}</text>',
      '<text x="200" y="444" class="s lab" text-anchor="middle">Contributions</text>',
      '<text x="200" y="476" class="s sub" text-anchor="middle">last 12 months</text>',
      '<line x1="400" y1="310" x2="400" y2="520" stroke="#30363d"/><line x1="800" y1="310" x2="800" y2="520" stroke="#30363d"/>',
      '<circle cx="600" cy="395" r="70" fill="none" stroke="#21262d" stroke-width="7"/>',
      '<circle class="ring" cx="600" cy="395" r="70" fill="none" stroke="#f0883e" stroke-width="7" stroke-linecap="round" transform="rotate(-90 600 395)"/>',
      f'<text x="600" y="414" class="s big" text-anchor="middle">{cur}</text>',
      '<text x="600" y="500" class="s lab" text-anchor="middle" fill="#f0883e" style="fill:#f0883e;font-weight:700">Current streak</text>',
      '<text x="600" y="530" class="s sub" text-anchor="middle">days in a row</text>',
      f'<text x="1000" y="400" class="s big" text-anchor="middle">{longest}</text>',
      '<text x="1000" y="444" class="s lab" text-anchor="middle">Longest streak</text>',
      '<text x="1000" y="476" class="s sub" text-anchor="middle">days, last 12 months</text>',
      f'<text x="1188" y="550" class="m sub" text-anchor="end" font-size="11">auto-updated {dt.date.today().isoformat()} from the GitHub API</text>',
      '</svg>']

os.makedirs("assets", exist_ok=True)
open("assets/dashboard.svg", "w", encoding="utf-8", newline="\n").write("\n".join(o))
print(f"repos={len(repos)} total={total} commits={commits} merged={merged} ci={ci_ok} cur={cur} longest={longest} top={[k for k, _ in top]}")
