<h1 align="center">Naman Verma</h1>

<p align="center">
  <b>Backend engineering · AI infrastructure · Security and distributed systems</b><br>
  I build systems and then test whether they hold up when things fail.<br>
  I like problems where correctness matters more than a convincing demo.
</p>

<p align="center">
  <a href="https://portfolio-naman-fbbb.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-visit-111111?style=flat-square"></a>
  <img alt="B.Tech CS, KIET, class of 2028" src="https://img.shields.io/badge/B.Tech%20CS-KIET%20'28-555555?style=flat-square">
  <a href="https://github.com/docling-project/docling/pull/5462"><img alt="Merged into docling" src="https://img.shields.io/badge/merged%20into-docling%20%235462-8957e5?style=flat-square&logo=github"></a>
</p>

---

### Highlights

- **Merged upstream:** a bug fix to IBM's [docling](https://github.com/docling-project/docling), approved by a maintainer and merged 2026-11-24 ([#5462](https://github.com/docling-project/docling/pull/5462)).
- **Built alone:** three Go tools that test whether AI infrastructure holds up when things fail, each with CI that shows the tool catches bugs planted on purpose.
- **Honest about limits:** every project below says what is verified and what is not yet.

### Flagship work: does AI infrastructure hold up when things fail?

Three Go tools I built alone. All three are **experimental**: each one is proven in CI against systems I wrote, not yet against real providers or outside users.

#### [capproof](https://github.com/NAMAN-VERMA-02/capproof)
[![ci](https://github.com/NAMAN-VERMA-02/capproof/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/NAMAN-VERMA-02/capproof/actions/workflows/ci.yml) [![release](https://img.shields.io/github/v/release/NAMAN-VERMA-02/capproof?style=flat-square)](https://github.com/NAMAN-VERMA-02/capproof/releases) ![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)

Tests whether an LLM gateway's spend cap holds under concurrency, dropped streams and malformed usage data, checking results against a mock provider that keeps its own bill, so it never trusts the gateway's numbers. Ships `capd`, a reference gateway that reserves each call's worst-case cost in a durable ledger before forwarding.

> ✅ **Verified:** CI shows the suite tells a naive gateway (BREACHED) from a strict one (HELD); if it couldn't, no other result would mean anything.<br>
> ⏳ **Not yet verified:** a real provider's billing.

#### [agentreplay](https://github.com/NAMAN-VERMA-02/agentreplay)
[![ci](https://github.com/NAMAN-VERMA-02/agentreplay/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/NAMAN-VERMA-02/agentreplay/actions/workflows/ci.yml) ![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)

Records what a tool-using agent sends to its LLM and MCP servers, replays the run offline, and tests a changed agent against the recorded tool results, with a SAME / CHANGED verdict and a CI exit code. Checks structure, not semantic correctness.

> ✅ **Verified:** catches regressions I planted in a demo agent run against a scripted model and a fake MCP server.<br>
> ⏳ **Not yet verified:** real providers and real agents.

#### [mcpfuzz](https://github.com/NAMAN-VERMA-02/mcpfuzz)
[![ci](https://github.com/NAMAN-VERMA-02/mcpfuzz/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/NAMAN-VERMA-02/mcpfuzz/actions/workflows/ci.yml) ![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

Checks MCP servers for protocol conformance bugs and, in an isolated Docker run, for path traversal (a canary from outside the allowed root must come back) and shell injection (an injected command must create a marker file).

> ✅ **Verified:** CI flags each planted bug in a deliberately vulnerable server and passes its fixed twin, which differs only at those bugs.<br>
> ⏳ **Not yet verified:** any third-party MCP server.

### Pull requests to other projects

**Merged**
- **[docling](https://github.com/docling-project/docling)** (IBM's document conversion library): [#5462](https://github.com/docling-project/docling/pull/5462) drops malformed link targets instead of turning them into broken `https:/` paths in the Markdown, HTML, AsciiDoc and JATS backends ([#5448](https://github.com/docling-project/docling/issues/5448)), through one shared `parse_hyperlink` helper with tests. Approved by a maintainer and merged 2026-11-24.
- **Roof** (Mansi Verma's warranty vault, college project): [#1](https://github.com/mansiverma897993/Roof/pull/1) streaming uploads, sign-in lockout, quotas, account controls. Merged 2026-11-19.
- **SELLABLE** (team project I'm a member of): [#22](https://github.com/HarshDubey23/SELLABLE/pull/22) audit log, LlamaIndex example, client config. Merged 2026-11-12.

**Open, not merged yet**
- **SELLABLE:** [#21](https://github.com/HarshDubey23/SELLABLE/pull/21) plural matching, ruff, inspect CLI.
- **NetraShield:** [#21](https://github.com/Gauravkkaushal/Browser-s-Agent/pull/21) on-device image redaction, face/QR masking, send guardrails.

My copies of SELLABLE, Browser-s-Agent and Roof on this profile are forks used to send my PRs; the projects belong to their teams.

### Other projects

| Project | Focus | Status | Evidence |
|---|---|---|---|
| [ScamCheck](https://github.com/NAMAN-VERMA-02/scamcheck) | English and Hinglish scam detection | Research, synthetic data only | Baselines B0–B4 with confidence intervals, 14-transform adversarial lab. Reports its failures: the rule engine fell from 9/12 to 4/16 on another author's messages. |
| [SETU](https://github.com/NAMAN-VERMA-02/setu) | Federated, privacy-preserving alumni network | Hackathon team project, 6 contributors · [live](https://setu-live-five.vercel.app) | **My part:** the college node (`node/`), round-2 architecture docs and the privacy probe. |
| [TableTap](https://github.com/NAMAN-VERMA-02/tabletap) | QR restaurant ordering with a real-time kitchen display | Solo project · [live](https://tabletap-blush-phi.vercel.app) | 51 API and real-time tests against in-memory MongoDB in CI. |
| [SELLABLE](https://github.com/HarshDubey23/SELLABLE) | Security gateway and remote MCP server for AI commerce | Team project (Harsh Dubey's repo), I'm a member | **My part:** [#21](https://github.com/HarshDubey23/SELLABLE/pull/21) plural matching, ruff, inspect CLI · [#22](https://github.com/HarshDubey23/SELLABLE/pull/22) audit log, LlamaIndex example, client config. #22 merged; #21 open, not merged yet. |
| [NetraShield](https://github.com/Gauravkkaushal/Browser-s-Agent) | Privacy-preserving browser agent (SIH problem 26171) | SIH team project, I'm a member | **My part:** [#21](https://github.com/Gauravkkaushal/Browser-s-Agent/pull/21) on-device image redaction, face/QR masking, send guardrails. Open, not merged yet. |

<table>
<tr>
<td valign="top" width="50%">

### Engineering interests

- Backend architecture and API design
- Distributed systems and data consistency
- AI agent infrastructure and evaluation
- Application security and protocol testing
- Automated testing and reproducible benchmarks

</td>
<td valign="top" width="50%">

### Engineering principles

- Reproducible results over unsupported claims.
- Explicit limitations over inflated metrics.
- Tests that verify failure modes, not just happy paths.
- Clear ownership and contribution boundaries.
- Security and correctness as design requirements.

</td>
</tr>
</table>

### Tools

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![Postgres](https://img.shields.io/badge/Postgres%20(Supabase)-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
