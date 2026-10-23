# Public documentation maintenance

**Adoption:** Micrantha's [shared documentation-sync skill](https://github.com/hackelia-micrantha/.github/blob/main/skills/documentation-sync/SKILL.md), unchanged. This project-owned page records Sandcastle-specific authority and validation limitations; it is not a second copy of the shared workflow.

## Authority and publication

- Private `hackelia-micrantha/sandcastle` owns the implementation, build and release engineering, unpublished behavior, and authority to approve specific immutable artifacts for publication.
- This public `sandcastle-community` repository owns its **explicitly published** documentation, versioned public contracts/schemas, reviewed interoperability examples, and approved release/distribution metadata. It is not a private code or history mirror.
- [Repository boundary](repository-boundary.md) defines the one-way, allow-listed publication and independent review model. Unknown source material, security-sensitive private research, credentials, operational evidence, and unrestricted generated files remain unpublished.
- [Public binary distribution issue #3](https://github.com/hackelia-micrantha/sandcastle-community/issues/3) governs a proposed binary-oriented flake, immutable artifact identity, signing/provenance, downstream pins, and consumer checks. The current public tree has **no committed flake, binary package, published man-page or source implementation**; do not imply the release path is available from a future-tense contract.

## Truthful public claims

Review the [README](../README.md), [boundary contract](repository-boundary.md), [contribution guide](../CONTRIBUTING.md), and [security reporting guidance](../SECURITY.md) whenever status, checkpoint semantics, artifact support, release path, or publication authorization changes.

- The checkpoint lifecycle remains experimental. A checkpoint can preserve workspace state but never itself grants authorization, approval, trusted execution, or proof of task completion.
- Package installation grants availability only; it does not confer restore, filesystem, runner, specialist, or governance authority.
- Explicitly separate **conceptual design**, **reviewed public contract**, **privately implemented/qualified source**, and **published supported immutable release**.
- Do not present a proposed flake schema, a source-only statement, or successful documentation review as a supported public CLI install, signed production release, or verified restore implementation.
- Do not publicly expose private incident records, attack corpora, host state or unreleased implementation detail to support maturity or security claims.

## Validation and release gates

There is currently **no repository-local public CI/workflow or established automated docs validation command**. Until project-owned [bootstrap issue #1](https://github.com/hackelia-micrantha/sandcastle-community/issues/1) supplies a reviewed least-privilege, credential-free validator:

1. Review the exact candidate commit and only its intended public files; inspect all changed Markdown links and verify local target paths on that revision.
2. Compare all changed public capability, platform, security, and release claims with accepted project-owned evidence; mark unverifiable claims as unknown or planned.
3. Review public/private classification, applicable contribution licensing decisions, and any new published artifact against the allow-list before merging.
4. Do not claim build, rendered-site, release-artifact, install, end-to-end, or production verification merely because static links and content were reviewed.

A future automated validator must not require private Sandcastle credentials or execute untrusted public PR code on a privileged host. Use a project-owned validation workflow if #1 later establishes one; don't create an alternate CI system here.

## Maintenance triggers

Reconcile the public documentation after accepted CLI/checkpoint contracts, artifact formats, binary package/tag releases, security/trust changes, private/public topology changes, or downstream install/restore qualification. Prefer event-driven review and existing issue ownership.

Use the shared skill's `DOC-Q*` decision queue for unresolved authorization, security, licensing, or publication ambiguity. A documentation change never independently authorizes release, declassification, deployment, or privileged runtime effects.
