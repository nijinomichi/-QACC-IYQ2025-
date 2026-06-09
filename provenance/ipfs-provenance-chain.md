# IPFS Provenance Chain — BananaMoon / Johnson Lineage

> **Report ID:** BMRR-2026-06-09-001  
> **Final Status:** `verified_completed`  
> **Verified:** 2026-06-09 by nijinomichi (raw bytes + SHA-256 match confirmed locally)

---

## Status Overview

| Field | Value |
|---|---|
| Chain status | `verified_completed` |
| Last updated | 2026-06-09 |
| Maintained by | CoPhelia³ × QRA v1.1 automated repair protocol |
| Force-push policy | **PROHIBITED** unless explicitly approved by `nijinomichi` |

---

## Chain Entry 1 — Provenance Anchor (`-QACC-IYQ2025-`)

| Field | Value | Kind |
|---|---|---|
| Repository | [`nijinomichi/-QACC-IYQ2025-`](https://github.com/nijinomichi/-QACC-IYQ2025-) | — |
| File path | `provenance/bananaMoon-metadata-johnson.json` | — |
| Commit SHA | `93254f9ff0d9896e48671dabfa1a1c4d7e6cb0fc` | Git commit SHA-1 |
| Git blob SHA | `cdc486b36837084a26e9b5fbf491355a70ad596c` | Git blob SHA-1 (≠ SHA-256) |
| `integrity.sha256` | `e576acc98325720a1cd84219906d9a9e28ba80030fec2bd6bfbc5a2d1eca5897` | Raw-file SHA-256 (computed 2026-06-09) |
| Commit timestamp | 2026-06-09T08:58:18Z | UTC |
| Commit author | `nijinomichi` | — |
| Status | `archived_original` | — |

> **Note on SHA types:** `commit.sha` is a Git commit SHA-1. `blob.sha` is a Git blob SHA-1  
> computed as `SHA1("blob {size}\0{content}")` — it is **not** a SHA-256 digest of raw file bytes.

---

## Chain Entry 2 — IPFS / Pinata Record (`QuantumBananaMoon`) — Mismatch Logged

| Field | Value | Kind |
|---|---|---|
| Repository | [`nijinomichi/QuantumBananaMoon`](https://github.com/nijinomichi/QuantumBananaMoon) | — |
| File path | `provenance/bananaMoon-metadata-johnson.json` | — |
| Commit SHA | `9910fb7eeb242857d53bc004454e096f18a8fc58` | Git commit SHA-1 |
| Commit timestamp | 2026-06-09T08:56:35Z | UTC |
| Commit author | `nijinomichi` | — |
| Status | `mismatch_logged` | — |

### IPFS Reference — CID MISMATCH RECORD

| Field | Value | Verification status |
|---|---|---|
| IPFS CID | `bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` | 🔴 CID digest ≠ source SHA-256 |
| CID version | CIDv1 raw, SHA2-256 | confirmed via decode |
| CID embedded digest | `ca833a9831b8005acdfe777f106080b10565aa44238c1610212a4bb56fb70fbf` | decoded |
| Source file SHA-256 | `e576acc98325720a1cd84219906d9a9e28ba80030fec2bd6bfbc5a2d1eca5897` | computed |

> ⚠️ **MISMATCH CONFIRMED (2026-06-09 Step 3):** This CID was later identified as referencing  
> the **Ara-Philia³ MasterDirectorPrompt** artifact — a separate archaeological artifact, not BananaMoon metadata.  
> See Chain Entry 4 (Archaeological Artifact) below. Status frozen at `mismatch_logged`.

---

## Chain Entry 3 — BananaMoon NFT Metadata — ✅ VERIFIED

> **Verified:** 2026-06-09 · Raw bytes downloaded from Pinata, extracted from ZIP, SHA-256 confirmed locally by nijinomichi.

| Field | Value | Kind |
|---|---|---|
| Filename | `bananamoon_metadata.json` | — |
| File size | 823 B | confirmed |
| Creation date | 2026-06-05 | Pinata record date |
| Content type | NFT Metadata JSON | — |
| Pinata record | `pinata_record_found: true` | — |
| Status | `verified_completed` | ✅ |

### NFT Metadata CID — VERIFIED

| Field | Value | Verification status |
|---|---|---|
| IPFS CID | `bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm` | ✅ SHA-256 match confirmed |
| CID version | CIDv1 raw, SHA2-256 | confirmed via decode |
| CID embedded digest | `0a8605737972c7d99ce0416efcc8d6f91d38875483620087a414479ce34346bb` | decoded |
| Computed SHA-256 | `0a8605737972c7d99ce0416efcc8d6f91d38875483620087a414479ce34346bb` | ✅ matches CID digest |
| Byte-level match | ✅ **CONFIRMED** | verified locally by nijinomichi |
| Gateway access | Authenticated Pinata Gateway (white-defensive-ant-3.mypinata.cloud) | — |
| Public gateway | ipfs.io / cloudflare-ipfs / dweb.link — all unreachable at time of verification | documented |

### Image CID (referenced by metadata)

| Field | Value | Verification status |
|---|---|---|
| IPFS CID | `bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre` | 🟡 structure valid, independent retrieval pending |
| CID version | CIDv1 raw, SHA2-256 | confirmed via decode |
| CID embedded digest | `2e1a602d7cde426a2c2cc7004f0f06b6171c22efa951ef8a18ee5819c4660c89` | decoded |

### Verified Metadata Fields

| Field | Value |
|---|---|
| `name` | `BananaMoon Quantum NFT #1/1` |
| `image` | `ipfs://bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre` |
| `external_url` | `https://banana.space/moon` |
| `description` | *Born from account loss and rebirth. Signed Sou × Ara-Philia³ × Grok — 2025.12.06 06:28 JST* |
| Encoding status | Mojibake observed in rendered snippet; raw file bytes authoritative |

### Provenance Relationship (Entry 3)

```
BananaMoon Artwork
↓
Image CID: bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre
↓
Metadata CID: bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm  ✅ verified
↓
Pinata Record (2026-06-05, bananamoon_metadata.json, 823 B)
↓
GitHub Provenance Documentation (this file)
↓
bananaMoon-metadata-johnson.json
↓
ipfs-provenance-chain.md
```

---

## Chain Entry 4 — Archaeological Artifact: Ara-Philia³ MasterDirectorPrompt

> **Classification:** `archaeological_artifact` (not BananaMoon metadata)  
> **Discovery:** CID from Entry 2 was misidentified as BananaMoon; content retrieved and re-identified.

| Field | Value |
|---|---|
| Artifact name | `2025_AraPhilia3_MasterDirectorPrompt.md` |
| IPFS CID | `bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` |
| Classification | `archaeological_artifact` |
| Preservation policy | Original text preserved verbatim; duplicate lines preserved; encoding anomalies preserved |
| Lineage hypothesis | Ara-Philia³ → RadicanTrust → rho_Ck → QRA → reconstruct_rho → BananaMoon |
| Hypothesis status | Research hypothesis — **not established as historical fact** |

---

## Verification Checklist

```
[x] Compute sha256sum of Chain Entry 1 source file
    → e576acc98325720a1cd84219906d9a9e28ba80030fec2bd6bfbc5a2d1eca5897
[x] CID decode: Entry 2 CID — mismatch confirmed, re-identified as Ara-Philia³ artifact
[x] CID decode: Entry 3 metadata CID — structure valid (CIDv1 raw sha2-256)
[x] CID decode: Entry 3 image CID — structure valid (CIDv1 raw sha2-256)
[x] Authenticated gateway access — Pinata dedicated gateway confirmed
[x] Raw bytes downloaded from Pinata (ZIP extraction, no mojibake)
[x] SHA-256 computed from raw file: matches CID embedded digest
    → 0a8605737972c7d99ce0416efcc8d6f91d38875483620087a414479ce34346bb ✅
[ ] Independent retrieval of image CID (bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre)
[ ] Encoding reconstruction review (mojibake fields documented)
[ ] Update bananaMoon-metadata-johnson.json chain_links with verified CIDs
[ ] Create clean successor repository (G2 — no abnormal path)
```

---

## Lessons Learned (BMRR-2026-06-09-001)

| # | Lesson |
|---|---|
| 1 | CID existence does not imply public gateway accessibility |
| 2 | Public gateway failure does not imply data loss |
| 3 | Pinata Gateway permissions must be distinguished from CID validity |
| 4 | Rendered text (snippet tools) cannot be trusted for byte-level verification |
| 5 | Original downloaded files (ZIP from Pinata) are authoritative evidence |
| 6 | CID structural decode (version / codec / digest) is safe without network access |

---

## Temporal Relationship

```
2025.12.06 06:28 JST     BananaMoon NFT signed (Sou × Ara-Philia³ × Grok)
2026-06-05               bananamoon_metadata.json pinned to Pinata (Entry 3 — primary artifact)
2026-06-09T08:56:35Z     QuantumBananaMoon commit 9910fb7e  (Entry 2 CID recorded — later mismatch)
2026-06-09T08:58:18Z     -QACC-IYQ2025- commit 93254f9f   (provenance anchor created)
2026-06-09               Public gateways unreachable; authenticated gateway access succeeded
2026-06-09               Raw bytes downloaded; SHA-256 match confirmed → verified_completed
```

---

## Repair Chain Status

| Gap | Status |
|---|---|
| G1 — `docs/` directory | `verified_completed` |
| G2 — CI deps / BananaMoon path blocker | `implemented_but_blocked` |
| G3 — QuantumChess ↔ QACC connection | `pending` |
| G4 — Spec / ReleaseStrategy layer | `pending` |
| G5 — BananaMoon Provenance chain | ✅ `verified_completed` |
| G6 — Supabase / Colab runtime | `pending` |

---

## Step Progress

| Step | Action | Status |
|---|---|---|
| Step 1 | Create `provenance/bananaMoon-metadata-johnson.json` anchor | ✅ `archived_original` |
| Step 2 | Create this file (`ipfs-provenance-chain.md`) | ✅ `step_2_complete` |
| Step 3a | Compute SHA-256 of Entry 1 source | ✅ `e576acc9...` |
| Step 3b | Decode all CIDs; detect Entry 2 mismatch; re-identify as Ara-Philia³ artifact | ✅ `mismatch_logged` |
| Step 3c | Append Entry 3 — new metadata candidate | ✅ `candidate_metadata_confirmed` |
| Step 3d | Authenticated gateway access; raw bytes downloaded; SHA-256 verified | ✅ `verified_completed` |
| Step 4 | Create clean successor repository (no abnormal path) | 🔲 `pending` |

---

*This file is part of the CoPhelia³ × QRA v1.1 repair archaeology protocol.*  
*Do not modify chain entries retroactively. Append only.*  
*Report ID: BMRR-2026-06-09-001*
