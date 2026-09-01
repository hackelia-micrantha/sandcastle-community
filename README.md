# Sandcastle Community

Public community surface for Sandcastle: documentation, schemas, examples, interoperability guidance, and public design discussion for deterministic checkpointed execution state.

> **Repository boundary:** this repository is a curated public surface. It is **not** the authoritative Sandcastle implementation repository and does not mirror private implementation history.

## What Sandcastle is

Sandcastle is a checkpoint layer for disposable execution environments. Its core model preserves useful mutable workspace state while allowing live execution environments to remain replaceable.

The conceptual lifecycle is:

```text
save -> mutate -> restore -> fork -> inspect/diff
```

A Sandcastle checkpoint describes concrete execution/workspace state. It does not confer authorization, approval, task completion, or trust.

## What belongs here

This repository is intended for deliberately published material such as:

- stable conceptual documentation;
- public checkpoint, CLI, and interoperability contracts;
- schemas intended for external consumers;
- safe examples and fixtures;
- public roadmap and release notes;
- design discussion appropriate for open review;
- feature requests and interoperability feedback.

## What does not belong here

The following remain in the private authoritative implementation repository unless deliberately published:

- Sandcastle implementation source and private Git history;
- unreleased implementation architecture;
- operational details for private infrastructure;
- security-sensitive exploit mechanics, hostile-input corpora, or internal incident material;
- private issues, pull requests, CI logs, credentials, or generated artifacts;
- Dubnium-specific operational state;
- arbitrary files merely because they live under a `docs/` directory.

Publication is an explicit reviewable action, not an automatic mirror.

## Authority model

```text
private Sandcastle implementation
        |
        | reviewed, allow-listed publication
        v
Sandcastle Community
        |
        +--> documentation
        +--> schemas/contracts
        +--> examples
        +--> public discussion
```

The private implementation repository is authoritative for implementation state. Published contracts in this repository are authoritative only to the extent explicitly identified and versioned as public contracts.

## Contributing

Public issues and contributions are welcome for documentation, contracts, examples, interoperability, and design feedback. Implementation work may be promoted into the private repository after triage rather than being developed here.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [Repository Boundary](docs/repository-boundary.md).

## Security

Do not publish vulnerability details or sensitive implementation information in a public issue. See [SECURITY.md](SECURITY.md).

## Status

Sandcastle is experimental and its checkpoint lifecycle is still being proven. Public contracts should be treated as unstable unless they are explicitly versioned and marked stable.
