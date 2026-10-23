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

Check the actual target `main` revision before selecting a validation command. [Bootstrap issue #1](https://github.com/hackelia-micrantha/sandcastle-community/issues/1) owns the public, credential-free validator; [PR #5](https://github.com/hackelia-micrantha/sandcastle-community/pull/5) is the independently reviewed CI candidate, **not evidence of adoption until merged and receiving-main verified**.

Where `scripts/check_public_docs_links.py`, `tests/test_public_docs_links.py`, and `.github/workflows/public-docs.yml` are present on the reviewed baseline, run the owning offline checks at the exact candidate SHA:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/check_public_docs_links.py
```

Also verify the matching GitHub-hosted `Validate public documentation` check and review its scope: local Markdown targets only, not remote URLs, heading anchors, rendered HTML, or published artifacts. If the three validator files are not yet present, **do not claim CI exists or has passed**; manually inspect every changed relative Markdown target at the exact revision and record that limitation.

For all documentation changes, whether automated validation is available or not:

1. Compare changed capability, platform, security, and release claims with accepted project-owned evidence; mark unsupported claims as unknown or planned.
2. Check public/private classification, contribution licensing, and any new artifact against the existing publication allow-list.
3. Do not claim build, rendered-site, release-artifact, install, end-to-end, or production verification merely because static links and content were reviewed.

The public validator must not require private Sandcastle credentials or execute untrusted PR code on a privileged host. Keep validation in the project-owned workflow, not an alternative pipeline.

## Maintenance triggers

Reconcile the public documentation after accepted CLI/checkpoint contracts, artifact formats, binary package/tag releases, security/trust changes, private/public topology changes, or downstream install/restore qualification. Prefer event-driven review and existing issue ownership.

Use the shared skill's `DOC-Q*` decision queue for unresolved authorization, security, licensing, or publication ambiguity. A documentation change never independently authorizes release, declassification, deployment, or privileged runtime effects.
