# Naman Verma

**Backend engineering · AI infrastructure · Security and distributed systems**

I build systems and then test whether they hold up when things fail. I like problems where correctness matters more than a convincing demo.

B.Tech CS at KIET Group of Institutions, Ghaziabad (class of 2028) · [Portfolio](https://portfolio-naman-fbbb.vercel.app)

---

### Flagship work: does AI infrastructure hold up when things fail?

Three Go tools I built alone. All three are **experimental**: each one is proven in CI against systems I wrote, not yet against real providers or outside users.

**[capproof](https://github.com/NAMAN-VERMA-02/capproof)** · Go
Tests whether an LLM gateway's spend cap holds under concurrency, dropped streams and malformed usage data, checking results against a mock provider that keeps its own bill, so it never trusts the gateway's numbers. Ships `capd`, a reference gateway that reserves each call's worst-case cost in a durable ledger before forwarding.
- **Verified:** CI shows the suite tells a naive gateway (BREACHED) from a strict one (HELD); if it couldn't, no other result would mean anything.
- **Not yet verified:** a real provider's billing.

**[agentreplay](https://github.com/NAMAN-VERMA-02/agentreplay)** · Go
Records what a tool-using agent sends to its LLM and MCP servers, replays the run offline, and tests a changed agent against the recorded tool results, with a SAME / CHANGED verdict and a CI exit code. Checks structure, not semantic correctness.
- **Verified:** catches regressions I planted in a demo agent run against a scripted model and a fake MCP server.
- **Not yet verified:** real providers and real agents.

**[mcpfuzz](https://github.com/NAMAN-VERMA-02/mcpfuzz)** · Go, Docker
Checks MCP servers for protocol conformance bugs and, in an isolated Docker run, for path traversal (a canary from outside the allowed root must come back) and shell injection (an injected command must create a marker file).
- **Verified:** CI flags each planted bug in a deliberately vulnerable server and passes its fixed twin, which differs only at those bugs.
- **Not yet verified:** any third-party MCP server.

### Other projects

| Project | Focus | Status | Evidence |
|---|---|---|---|
| [ScamCheck](https://github.com/NAMAN-VERMA-02/scamcheck) | English and Hinglish scam detection | Research, synthetic data only | Baselines B0–B4 with confidence intervals, 14-transform adversarial lab. Reports its failures: the rule engine fell from 9/12 to 4/16 on another author's messages. |
| [SETU](https://github.com/NAMAN-VERMA-02/setu) | Federated, privacy-preserving alumni network | Hackathon team project, 6 contributors · [live](https://setu-live-five.vercel.app) | **My part:** the college node (`node/`), round-2 architecture docs and the privacy probe. |
| [TableTap](https://github.com/NAMAN-VERMA-02/tabletap) | QR restaurant ordering with a real-time kitchen display | Solo project · [live](https://tabletap-blush-phi.vercel.app) | 51 API and real-time tests against in-memory MongoDB in CI. |

### Engineering interests

- Backend architecture and API design
- Distributed systems and data consistency
- AI agent infrastructure and evaluation
- Application security and protocol testing
- Automated testing and reproducible benchmarks

### Pull requests to other projects

I have opened 4 pull requests on other people's projects. All 4 are **open and awaiting review; none has been merged yet.**

- **SELLABLE** (Harsh Dubey's MCP commerce gateway): [#21](https://github.com/HarshDubey23/SELLABLE/pull/21) plural matching, ruff, inspect CLI · [#22](https://github.com/HarshDubey23/SELLABLE/pull/22) audit log, LlamaIndex example, client config
- **NetraShield / Browser-s-Agent** (SIH team project): [#21](https://github.com/Gauravkkaushal/Browser-s-Agent/pull/21) on-device image redaction, face/QR masking, send guardrails
- **Roof** (Mansi Verma's warranty vault, college project): [#1](https://github.com/mansiverma897993/Roof/pull/1) streaming uploads, sign-in lockout, quotas, account controls

My copies of those repos on this profile are forks used to send these PRs; the projects belong to their teams.

### Engineering principles

- Reproducible results over unsupported claims.
- Explicit limitations over inflated metrics.
- Tests that verify failure modes, not just happy paths.
- Clear ownership and contribution boundaries.
- Security and correctness as design requirements.

### Tools

Go · Python (FastAPI, pytest) · TypeScript / Node (Express) · MongoDB · Postgres (Supabase) · GitHub Actions
