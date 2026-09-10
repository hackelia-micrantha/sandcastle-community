# Sandcastle Community

Public community and distribution surface for Sandcastle: documentation, schemas, examples, interoperability guidance, public design discussion, and explicitly published binary package metadata for deterministic checkpointed execution state.

> **Repository boundary:** this repository is a curated public surface. It is **not** the authoritative Sandcastle implementation repository and does not mirror private implementation history.

## What Sandcastle is

Sandcastle is a checkpoint layer for disposable execution environments. Its core model preserves useful mutable workspace state while allowing live execution environments to remain replaceable.

The conceptual lifecycle is:

```text
checkpoint -> mutate -> restore -> fork -> inspect/diff
```

A Sandcastle checkpoint describes concrete execution/workspace state. It does not confer authorization, approval, task completion, or trust.

## Project history

Sandcastle grew from an earlier Docker sandbox utility built around reusable isolated development environments. The archived [Sandbox Demo](https://ryanjennin.gs/archive/sandcastle-util-demo/) captures that origin. This repository remains the curated public authority for current published Sandcastle documentation, contracts, examples, distribution metadata, and status.

## What belongs here

This repository is intended for deliberately published material such as:

- stable conceptual documentation;
- public checkpoint, CLI, and interoperability contracts;
- schemas intended for external consumers;
- safe examples and fixtures;
- public roadmap and release notes;
- design discussion appropriate for open review;
- feature requests and interoperability feedback;
- binary-oriented Nix package/flake metadata for authorized immutable Sandcastle releases;
- checksums, signatures, provenance/SBOM references, and public man pages associated with those releases.

## What does not belong here

The following remain in the private authoritative implementation repository unless deliberately published:

- Sandcastle implementation source and private Git history;
- unreleased implementation architecture;
- private build/development toolchains and fixtures;
- operational details for private infrastructure;
- security-sensitive exploit mechanics, hostile-input corpora, or internal incident material;
- private issues, pull requests, CI logs, credentials, or arbitrary generated artifacts;
- Dubnium-specific operational state;
- arbitrary files merely because they live under a `docs/` directory.

Publication is an explicit reviewable action, not an automatic mirror.

## Authority and release model

```text
private Sandcastle implementation + release authority
        |
        | reviewed, allow-listed release/publication
        v
Sandcastle Community
        |
        +--> documentation
        +--> schemas/contracts
        +--> examples
        +--> CLI/man pages
        +--> binary-oriented flake/package metadata
        +--> hashes/provenance/release notes
        |
        v
exact downstream pins (for example Dubnium/dotfiles)
```

The private implementation repository is authoritative for source, implementation state, build/release engineering, and authorization of release artifacts. Published contracts in this repository are authoritative only to the extent explicitly identified and versioned as public contracts. Published package metadata is authoritative for the explicitly published distribution surface; it does not make this repository implementation authority.

Normal downstream evaluation/install of a public Sandcastle package should not require credentials for the private canonical repository.

Package installation grants software availability only. It does not grant checkpoint restore, host-filesystem, runner/specialist, or governance authority.

See [Repository Boundary](docs/repository-boundary.md). Public binary distribution is tracked in [#3](https://github.com/hackelia-micrantha/sandcastle-community/issues/3).

## Contributing

Public issues and contributions are welcome for documentation, contracts, examples, interoperability, distribution metadata, and design feedback. Implementation work may be promoted into the private repository after triage rather than being developed here.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [Repository Boundary](docs/repository-boundary.md).

## Security

Do not publish vulnerability details or sensitive implementation information in a public issue. See [SECURITY.md](SECURITY.md).

## Status

Sandcastle is experimental and its checkpoint lifecycle is still being proven. Public contracts and distribution artifacts should be treated as unstable unless they are explicitly versioned and marked supported.
