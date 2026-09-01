# Security

Sandcastle handles checkpoint and workspace materialization boundaries where implementation details may be security-sensitive.

## Do not report vulnerabilities publicly

Do not include exploit details, credentials, private infrastructure information, hostile payloads, or sensitive logs in public issues, discussions, or pull requests.

Use GitHub's private vulnerability reporting flow for the relevant Micrantha repository when it is available. If a private reporting path is not available, open only a minimal public issue requesting a private contact channel; do not include vulnerability details.

## Public security discussion

Public discussion is appropriate for:

- documented security guarantees and limitations;
- threat-model concepts already deliberately published;
- interoperability requirements;
- defensive guidance that does not reveal unpublished exploitable implementation details.

## Scope boundary

This repository does not contain the authoritative Sandcastle implementation. Security fixes may therefore be developed privately before a public advisory, contract update, or release note is published here.
