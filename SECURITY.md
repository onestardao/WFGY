# Security Policy

This document describes how to report potential security issues in this repository and how maintainers handle disclosure.

## Reporting a vulnerability

If you believe you have found a security vulnerability, please report it privately and responsibly.

Preferred reporting channel:

1. **Email**: `hello@onestardao.com`  
   Subject: `[WFGY Security] <short summary>`

Alternative channels (if email is not possible):

2. **Telegram**: `@PSBigBig`  
   Please start your message with: `[WFGY Security]`  
   Avoid sending sensitive details in public chats or groups.

3. **GitHub Security Advisory (recommended when enabled)**  
   Use the repository Security tab to submit a private vulnerability report via GitHub Advisories.

**Please do not disclose vulnerability details in public issues, discussions, PR comments, or social posts** until maintainers confirm that disclosure is safe. This reduces the risk of exploitation before mitigations are available.

### What to include in a report

To help maintainers verify and assess the report quickly, please include:

- A clear description of the issue and why it is a security concern
- Affected component(s) and file path(s), if known
- The commit hash, tag, or release version you tested
- Minimal reproduction steps or a proof-of-concept (PoC), when feasible
- Any logs, stack traces, or screenshots that support the report
- Your suggested severity and rationale (optional)

If a full PoC would increase risk, you can provide a high-level description first and share sensitive details after maintainers respond.

## Response process

Maintainers aim to acknowledge reports in a timely manner, but response time can vary depending on availability and report complexity.

Typical workflow:

1. **Acknowledgement**: maintainers confirm receipt and may request clarification.
2. **Triage**: maintainers assess impact, scope, and reproducibility.
3. **Mitigation**: a fix or mitigation is developed and tested.
4. **Release and disclosure**: relevant changes are released and documented.

When appropriate, maintainers may coordinate disclosure timing with the reporter. If a CVE is appropriate and feasible, maintainers may coordinate CVE assignment through standard channels.

## Supported versions

Security fixes are provided on a best-effort basis.

- The primary supported line is the latest state of the `main` branch and/or the latest tagged release.
- Backports to older tags or branches are not guaranteed.

If you rely on older versions, please consider upgrading or opening a discussion to request a backport, understanding that maintainers may decline based on scope and maintenance cost.

## Contact

- Email: `hello@onestardao.com`
- Telegram: `@PSBigBig`
- GitHub Security Advisories: `https://github.com/onestardao/WFGY/security/advisories`
