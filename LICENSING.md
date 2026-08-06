# Licensing overview

This repository uses **two licenses**, kept legibly separated.

> **Pointer:** the *skill-format layer* (the phi-resonance-search-loop skill,
> derived from Anthropic's `algorithmic-art` template) is licensed under
> **Apache-2.0** — see [`./NOTICE`](./NOTICE) and
> [`./licenses/APACHE-2.0.txt`](./licenses/APACHE-2.0.txt).

| Layer | License | Canonical file |
|-------|---------|----------------|
| Repository as a whole | GNU GPL v3.0 | [`./LICENSE`](./LICENSE) |
| Skill-format layer (derived) | Apache License 2.0 | [`./licenses/APACHE-2.0.txt`](./licenses/APACHE-2.0.txt) |
| Attribution & modification notice | — | [`./NOTICE`](./NOTICE) |

## Why the root `LICENSE` is not edited

The GPL-3.0 text is a verbatim license document; its own header states that
changing it is not allowed, and automated tooling (e.g. GitHub's license
detector) parses it as-is. The multi-license clarification therefore lives
here and in `./NOTICE`, leaving `./LICENSE` pristine and machine-detectable.

## Compatibility

Apache-2.0 is one-way compatible into GPLv3. The upstream copyright
(`Copyright 2026 Anthropic, PBC.`) and Apache-2.0 notice are preserved
regardless of direction, per Apache-2.0 §4(c)/§4(d).

See `provenance/PROVENANCE_phi-resonance-search-loop.md` for the full
provenance and modification log.

