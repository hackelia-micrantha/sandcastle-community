# Repository Boundary

Sandcastle uses a private-core / public-community repository model.

## Repositories

- `hackelia-micrantha/sandcastle` — private authoritative implementation and release-engineering repository.
- `hackelia-micrantha/sandcastle-community` — public community, contract, and binary-distribution surface.

## Authority

The private repository is authoritative for implementation source, implementation architecture, private engineering work, CI state, unreleased behavior, build tooling, and construction/authorization of Sandcastle release artifacts.

The public repository is authoritative only for artifacts explicitly published here, such as a versioned public schema/contract, public CLI/man-page contract, or binary package metadata for an authorized release. Public discussion, roadmap material, examples, and package metadata are not evidence of private implementation state unless a published artifact says otherwise.

The public repository does **not** become implementation authority merely because it distributes an executable package.

## Publication model

Publication is a one-way, explicit declassification step:

```text
private source / build authority
      |
      | allow-list + review + validation
      v
immutable authorized release artifact
      |
      | publication
      v
sandcastle-community
      |
      +--> public contracts/docs/man pages
      +--> hashes/provenance/release metadata
      +--> binary-oriented Nix flake
```

There is no automatic bidirectional synchronization and no requirement that private paths map directly to public paths.

### Required properties

A future automated publication mechanism should:

- use an allow-list rather than trying to exclude sensitive paths after the fact;
- produce a deterministic public tree or deterministic artifact set;
- make release/provenance identity inspectable where safe;
- validate that only managed public artifacts are emitted into exported namespaces;
- run secret/sensitive-data checks before publication;
- present a reviewable diff or artifact manifest before mutation/publication;
- fail closed on unknown or unmanaged input;
- avoid credentials that let the public repository mutate the private repository;
- never publish private Git history, issues, pull requests, CI logs, runtime state, arbitrary generated output, or private hostile-input/security corpora.

## Release and distribution model

Sandcastle follows the Micrantha **private canonical + public binary distribution** strategy.

```text
hackelia-micrantha/sandcastle
  -> repository-owned build/release tooling
  -> immutable reviewed release artifact
  -> hackelia-micrantha/sandcastle-community
       -> binary-oriented flake/package metadata
       -> cryptographic hashes
       -> public CLI/man pages/contracts
  -> downstream exact pins (for example Dubnium `flake.lock`)
```

The public distribution flake should fetch immutable authorized release assets rather than implementation source.

Normal public/downstream evaluation and installation must not require credentials for the private canonical repository. Development-only outputs such as private dev shells, fuzz/security corpora, implementation test fixtures, and internal build details do not need to be recreated here.

For CLI releases, the published package should keep executable version, package/release identity, man-page metadata, checksums/signatures/provenance references, and supported public contracts coherent.

Package installation conveys **software availability only**. It grants no checkpoint restore authority, host-filesystem authority, runner/specialist authority, or governance approval.

Tracking: `sandcastle-community#3` owns the public binary-oriented release/package surface; `hackelia-micrantha/sandcastle#16` owns the private canonical build/release contract.

## Contribution promotion

Community work flows inward as requirements or design evidence, not as an automatic source merge:

```text
public issue / proposal / contract feedback
             |
             v
         public triage
             |
             v
private implementation work when required
             |
             v
validated publishable result
             |
             v
      public contract/update
```

This permits public interoperability and design discussion without making private implementation state dependent on a public mirror.

## Security boundary

Repository privacy is not itself a security control. Sensitive data and credentials must still be excluded from source control, release artifacts, and checkpoint artifacts. Conversely, publication should be treated as an irreversible disclosure effect: material should cross this boundary only when deliberately reviewed as public.

Threat models, guarantees, limitations, interoperability information, and binary verification metadata can be public when that improves defensive understanding without exposing unpublished exploit mechanics or unnecessary private operational details.
