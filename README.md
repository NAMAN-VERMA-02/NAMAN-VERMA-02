# Naman Verma

**Backend and AI infrastructure. I build systems and then test whether they hold up when things fail.**

CS undergrad at KIET Group of Institutions, Ghaziabad (class of 2028) · [Portfolio](https://portfolio-naman-fbbb.vercel.app)

I care about evidence: CI on every push, tests that try to break the system, and results published with their failures included. Each project below says what has been tested and what hasn't.

---

### Featured

**[capproof](https://github.com/NAMAN-VERMA-02/capproof)** · Go
Does an LLM gateway's spend cap actually hold under concurrency, dropped streams and malformed usage data? capproof injects faults and checks the result against a mock provider that keeps its own bill, so it never trusts the gateway's own numbers. It ships with `capd`, a reference gateway that reserves each call's worst-case cost in a durable ledger before forwarding. CI checks that the suite tells a naive gateway (BREACHED) from a strict one (HELD); if it couldn't, no other result would mean anything. *Not yet tested against a real provider's billing.*

**[agentreplay](https://github.com/NAMAN-VERMA-02/agentreplay)** · Go
Records what a tool-using agent sends to its LLM and MCP servers, replays the run offline, and tests a changed agent against the recorded tool results, with a SAME / CHANGED verdict and an exit code for CI. *Benchmarked only on a demo agent, a scripted model and a fake MCP server, with regressions I planted myself; real providers and real agents are untested.*

**[mcpfuzz](https://github.com/NAMAN-VERMA-02/mcpfuzz)** · Go, Docker
Checks MCP servers for protocol conformance bugs, and in an isolated Docker run, for path traversal (a canary from outside the allowed root must come back) and shell injection (an injected command must create a marker file). CI runs it against a deliberately vulnerable server and a fixed twin that differ only at each bug. *Tested only against those two servers so far.*

**[ScamCheck](https://github.com/NAMAN-VERMA-02/scamcheck)** · Python, FastAPI, Next.js
An evidence-first scam checker for English and Hinglish messages, with a benchmark lab (baselines B0–B4, Wilson and bootstrap intervals) and a seeded adversarial lab (14 transforms with exact replay). The README reports the negative results too: the rule engine dropped from 9/12 to 4/16 on another author's messages, and a local LLM flagged 4/12 legitimate OTP and bank messages. All data so far is synthetic, and the README says so up front.

**[SETU (सेतु)](https://github.com/NAMAN-VERMA-02/setu)** · Next.js, Supabase, Python, FastAPI · [live](https://setu-live-five.vercel.app)
An alumni network that matches students to seniors who were once in their exact position. Hackathon team project (6 GitHub contributors). **My part:** I committed the college node (`node/`), the round-2 architecture docs and the privacy probe. The design: each college runs its own node holding its people's data, and the hub routes only pseudonymous IDs and consent events, so a college can disconnect and its data leaves with it.

**[TableTap](https://github.com/NAMAN-VERMA-02/tabletap)** · Node, Express, MongoDB, Socket.io · [live](https://tabletap-blush-phi.vercel.app)
QR restaurant ordering with a live kitchen display. Server-side pricing, per-restaurant data scoping, JWT in httpOnly cookies, Zod validation and rate limiting. Analytics come from a single `$facet` aggregation. 51 API and real-time tests run against in-memory MongoDB in CI.

### Also built

[oweit](https://github.com/NAMAN-VERMA-02/oweit) (finds promises you made in WhatsApp and email, English + Hinglish) · [Manyaki](https://github.com/NAMAN-VERMA-02/manyaki-companion) (Electron 3D desktop companion with an offline voice mode) · [NagriVanta](https://github.com/NAMAN-VERMA-02/NagriVanta) (MERN civic issue platform, [live](https://nagrivanta-web.vercel.app)) · [Bronze](https://github.com/NAMAN-VERMA-02/bronze) (Three.js strategy game, [play](https://naman-verma-02.github.io/bronze/))

### Contributions to other projects

Pull requests I opened on team and upstream repos (status as of November 2026):

- **SELLABLE** (Harsh Dubey's MCP commerce gateway): [#21](https://github.com/HarshDubey23/SELLABLE/pull/21) plural matching, ruff, inspect CLI · [#22](https://github.com/HarshDubey23/SELLABLE/pull/22) audit log, LlamaIndex example, client config. Both open.
- **NetraShield / Browser-s-Agent** (SIH team project): [#21](https://github.com/Gauravkkaushal/Browser-s-Agent/pull/21) on-device image redaction, face/QR masking and send guardrails. Open.
- **Roof** (Mansi Verma's warranty vault, college project): [#1](https://github.com/mansiverma897993/Roof/pull/1) streaming uploads, sign-in lockout, quotas, account controls. Open.

My copies of those repos on this profile are forks used to send these PRs; the projects belong to their teams.

### Tools I use

Go · Python (FastAPI, pytest) · TypeScript / Node (Express) · MongoDB · Postgres (Supabase) · GitHub Actions
