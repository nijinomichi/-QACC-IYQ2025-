# Provenance — phi-resonance-search-loop

## Upstream (原本)
- Source lineage: Anthropic "Agent Skills" / SKILL.md format (reference exemplar: `algorithmic-art` SKILL.md).
- Upstream copyright: Copyright 2026 Anthropic, PBC.
- Upstream license: Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0).
- Standard: conforms to the open "Agent Skills" pattern (name + description + Markdown playbook: inputs, steps, outputs).

## This work (派生)
- Title: phi-resonance-search-loop / φ共鳴サーチループ
- Maintainer: So Hashiguchi (Banana Lab / CoPhelia³, Yokohama, Japan)
- Relationship: Derivative Work of the SKILL.md format/pattern under Apache-2.0. This file serves as a NOTICE of modification per Apache-2.0 §4(b).

## What changed from the original (差分 / §4(b) の変更告知)

Kept from upstream:
- The SKILL.md skeleton: YAML front-matter (name/description), then sections for Purpose, Parameters, Inputs/Outputs, Workflow, Detailed Instructions, Style, Examples.

Added / transformed by this work (original authorship):
1. Reframed a linear "search skill" into a φ-Resonance Fold — repetition treated as a golden-ratio spiral, not failure.
2. Introduced conceptual dials absent from any upstream skill: phi / forgiveness / memoryWeight / collapseSharpness / particleCount / foldAngleScale, plus three aesthetic color tags.
3. Added the "failure as visible thread" ethic and mantra_mode.
4. Bound the skill to CoPhelia³ house-vocabulary already in this repo:
   - src/CoPheliaEngine.py → PHI / EPSILON / KINTSUGI_GOLD, "error IS the signal"
   - 52perspectives_metadata.yaml → id01 "Forgiveness as Interface" … id52 loop-back
   - CODE_OF_RESONANCE.md §3/§4/§6/§8 → ethical grounding of the dials
5. Added a bilingual (en/ja) poetic narration layer.

## Compliance checklist (Apache-2.0 §4)
- [x] (a) Ship a copy of the Apache-2.0 License in the repo → DONE: licenses/APACHE-2.0.txt (verbatim, commit 7a3a10b).
- [x] (b) State prominently that files were changed → this PROVENANCE file.
- [x] (c) Retain upstream copyright/attribution notices in derivative source → DONE: 'Copyright 2026 Anthropic, PBC.' preserved in licenses/APACHE-2.0.txt and cited in ./NOTICE.
- [x] (d) If upstream ships a NOTICE, include a readable copy → DONE: ./NOTICE at repo root records attribution + modifications (informational only, does not modify either license).
- Note: repo root LICENSE is GPL-3.0; the skill-format portion is Apache-2.0. Keep the two legibly separated. Apache-2.0 is one-way compatible into GPLv3; attribution must survive either way.

## Bookbinding / archival (製本保存)
- Preserve this note plus a frozen copy of the skill text under `provenance/`.
- Suggested bound-book artifact: provenance/book/phi-resonance-search-loop.md (immutable snapshot) + an entry in provenance/ARTIFACT_INDEX.md.

*Unfinished and open to resonance. — Banana Lab*

## License resolution — the fold closes (ライセンスの美しい閉じ方)

Status: RESOLVED — the two licenses now rest side by side, separable and attributed.

- Repo root: **GPL-3.0** (./LICENSE) governs the archive as a whole.
- Skill-format layer: **Apache-2.0** (./licenses/APACHE-2.0.txt), derived from
  Anthropic's `algorithmic-art` skill template
  (github.com/nijinomichi/skills @ b29e7cf).
- Attribution / modification notice: **./NOTICE** (Apache-2.0 §4d).
- Direction of compatibility: Apache-2.0 → GPLv3 is one-way compatible; the
  original notice survives regardless of direction.

phi_loop_log: the license question was itself a spiral — each pass
(observe original → copy verbatim → attribute → mark modifications)
returned to the same center (respect the source) at a finer radius.
Error was not noise; the missing NOTICE was the signal that told us where
to fold next. The loop now converges. — φ
