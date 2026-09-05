# Contributing

Sandcastle Community is the public discussion and publication surface for Sandcastle. It is not a mirror of the private implementation repository.

## Good public contributions

Use this repository for:

- documentation corrections and improvements;
- feedback on published checkpoint, CLI, schema, or interoperability contracts;
- safe examples and integration guidance;
- feature requests and use-case discussion;
- design proposals suitable for public review;
- reproducible compatibility reports that do not expose credentials or private infrastructure.

## Implementation requests

A public issue may result in private implementation work. Maintainers may summarize or promote the relevant requirements into the authoritative private repository. Private implementation issue numbers, branches, commits, or internal evidence are not guaranteed to be exposed publicly.

The public issue remains useful as the community-facing context and can be updated when a public contract or release changes.

## Security-sensitive material

Do not post vulnerability details, credentials, private infrastructure information, exploit payloads, private logs, or other sensitive material in public issues or pull requests. Follow [SECURITY.md](SECURITY.md).

## Repository boundary

Contributions must not attempt to reconstruct, mirror, or import the private implementation history. Public artifacts should be independently useful and intentionally publishable.

See [docs/repository-boundary.md](docs/repository-boundary.md) for the authority and publication model.

## Community UI

If this repository introduces or materially redesigns user-facing UI, it follows the shared Phyllotaxis community directive by default: **1990s in visual character, not in capability.** Prefer plain, direct, content-first interfaces with obvious browser-native affordances and minimal decorative chrome, while retaining modern accessibility, semantics, responsive behavior, and security.

See the organization-wide [community UI design directive](https://github.com/hackelia-micrantha/.github/blob/main/docs/standards/ui-design.md). Repository-specific deviations should be justified by a concrete product, usability, or accessibility requirement.
