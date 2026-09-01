# Repository Boundary

Sandcastle uses a private-core / public-community repository model.

## Repositories

- `hackelia-micrantha/sandcastle` — private authoritative implementation repository.
- `hackelia-micrantha/sandcastle-community` — public community and publication surface.

## Authority

The private repository is authoritative for implementation source, implementation architecture, private engineering work, CI state, and unreleased behavior.

The public repository is authoritative only for artifacts explicitly published here, such as a versioned public schema or contract. Public discussion, roadmap material, and examples are not evidence of private implementation state unless a published artifact says otherwise.

## Publication model

Publication is a one-way, explicit declassification step:

```text
private source artifact
      |
      | allow-list + review + validation
      v
public staging artifact
      |
      | publication
      v
sandcastle-community
```

There is no automatic bidirectional synchronization and no requirement that private paths map directly to public paths.

### Required properties

A future automated publication mechanism should:

- use an allow-list rather than trying to exclude sensitive paths after the fact;
- produce a deterministic public tree or deterministic artifact set;
- make the source revision/provenance inspectable where safe;
- validate that only managed public artifacts are emitted into exported namespaces;
- run secret/sensitive-data checks before publication;
- present a reviewable diff before mutation;
- fail closed on unknown or unmanaged input;
- avoid credentials that let the public repository mutate the private repository;
- never publish private Git history, issues, pull requests, CI logs, runtime state, or arbitrary generated output.

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

Repository privacy is not itself a security control. Sensitive data and credentials must still be excluded from source control and checkpoint artifacts. Conversely, publication should be treated as an irreversible disclosure effect: material should cross this boundary only when deliberately reviewed as public.

Threat models, guarantees, limitations, and interoperability information can be public when that improves defensive understanding without exposing unpublished exploit mechanics or private operational details.
