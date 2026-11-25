"""Rewrite the README block between RECENT markers with my most recently pushed repos."""
import json, os, re, urllib.request

USER = "NAMAN-VERMA-02"
SKIP = {USER, "web-development", "leetcode"}  # profile repo and practice repos
req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30&type=owner",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
repos = json.load(urllib.request.urlopen(req, timeout=30))
rows = [r for r in repos if not r["fork"] and not r["archived"] and r["name"] not in SKIP and r["description"]][:5]
assert rows, "GitHub returned no repos; refusing to blank the section"
def row(r):
    desc = ": " + r["description"].strip() if r["description"] else ""
    return f"- 🔨 **[{r['name']}]({r['html_url']})**{desc} <sub>· pushed {r['pushed_at'][:10]}</sub>"
lines = [row(r) for r in rows]
block = "<!--RECENT:START-->\n" + "\n".join(lines) + "\n<!--RECENT:END-->"
path = "README.md"
text = open(path, encoding="utf-8").read()
new, n = re.subn(r"<!--RECENT:START-->.*?<!--RECENT:END-->", lambda _: block, text, flags=re.S)
assert n == 1, "RECENT markers not found exactly once"
open(path, "w", encoding="utf-8", newline="\n").write(new)
print(f"updated {len(lines)} rows")
