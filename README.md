# Naman Verma

**Backend and AI infrastructure. I build systems and then test whether they hold up when things fail.**

CS undergrad at KIET Group of Institutions, Ghaziabad (class of 2028) · [Portfolio](https://portfolio-naman-fbbb.vercel.app)

I care about evidence: CI on every push, tests that try to break the system, and results published with their failures included.

---

### Featured

**[capproof](https://github.com/NAMAN-VERMA-02/capproof)** · Go
Does an LLM gateway's spend cap actually hold under concurrency, dropped streams and malformed usage data? capproof injects faults and checks the result against a mock provider that keeps its own bill, so it never trusts the gateway's own numbers. It ships with `capd`, a reference gateway that reserves each call's worst-case cost in a durable ledger before forwarding. CI checks that the suite tells a naive gateway (BREACHED) from a strict one (HELD); if it couldn't, no other result would mean anything.

**[ScamCheck](https://github.com/NAMAN-VERMA-02/scamcheck)** · Python, FastAPI, Next.js
An evidence-first scam checker for English and Hinglish messages, with a benchmark lab (baselines B0–B4, Wilson and bootstrap intervals) and a seeded adversarial lab (14 transforms with exact replay). The README reports the negative results too: the rule engine dropped from 9/12 to 4/16 on another author's messages, and a local LLM flagged 4/12 legitimate OTP and bank messages. All data so far is synthetic, and the README says so up front.

**[TableTap](https://github.com/NAMAN-VERMA-02/tabletap)** · Node, Express, MongoDB, Socket.io · [live](https://tabletap-blush-phi.vercel.app)
QR restaurant ordering with a live kitchen display. Server-side pricing, per-restaurant data scoping, JWT in httpOnly cookies, Zod validation and rate limiting. Analytics come from a single `$facet` aggregation. 50+ API and real-time tests run against in-memory MongoDB in CI.

**[SETU (सेतु)](https://github.com/NAMAN-VERMA-02/setu)** · Next.js, Supabase, Python, FastAPI · [live](https://setu-live-five.vercel.app)
An alumni network that matches students to seniors who were once in their exact position. Hackathon team project (6 GitHub contributors). **My part:** I committed the college node (`node/`), the round-2 architecture docs and the privacy probe. The design: each college runs its own node holding its people's data, and the hub routes only pseudonymous IDs and consent events, so a college can disconnect and its data leaves with it.

### Also built

[Manyaki](https://github.com/NAMAN-VERMA-02/manyaki-companion) (Electron 3D desktop companion with an offline voice mode) · [NagriVanta](https://github.com/NAMAN-VERMA-02/NagriVanta) (MERN civic issue platform, [live](https://nagrivanta-web.vercel.app)) · [Bronze](https://github.com/NAMAN-VERMA-02/bronze) (Three.js strategy game, [play](https://naman-verma-02.github.io/bronze/))

### Tools I use

Go · Python (FastAPI, pytest) · TypeScript / Node (Express) · MongoDB · Postgres (Supabase) · GitHub Actions
