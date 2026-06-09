# IPFS Provenance Chain — BananaMoon / Johnson Lineage

> **Disclaimer:** This provenance chain records the existence of a Pinata/IPFS reference, but does not yet certify independent retrieval or byte-level verification of the CID payload.

---

## Status Overview

| Field | Value |
|---|---|
| Chain status | `implemented_but_not_verified` |
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
> The `integrity.sha256` field above was computed from raw file bytes retrieved via GitHub MCP on 2026-06-09.

---

## Chain Entry 2 — IPFS / Pinata Record (`QuantumBananaMoon`) — Mismatch Logged

| Field | Value | Kind |
|---|---|---|
| Repository | [`nijinomichi/QuantumBananaMoon`](https://github.com/nijinomichi/QuantumBananaMoon) | — |
| File path | `provenance/bananaMoon-metadata-johnson.json` | — |
| Commit SHA | `9910fb7eeb242857d53bc004454e096f18a8fc58` | Git commit SHA-1 |
| Commit timestamp | 2026-06-09T08:56:35Z | UTC |
| Files changed | `provenance/bananaMoon-metadata-johnson.json` (+99 lines) | — |
| Commit author | `nijinomichi` | — |
| Status | `mismatch_logged` | — |

### IPFS / Pinata Reference — CID MISMATCH RECORD

| Field | Value | Verification status |
|---|---|---|
| Pinata File ID | `019e97c3-6e28-7fd8-907c-63660840fc25` | 🔴 CID digest mismatch — not verified |
| IPFS CID | `bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` | 🔴 digest mismatch |
| CID version | CIDv1 (base32 multibase) | confirmed via decode |
| Multicodec | `raw` (0x55) | confirmed via decode |
| Hash function | SHA2-256 (0x12) | confirmed via decode |
| CID embedded digest | `ca833a9831b8005acdfe777f106080b10565aa44238c1610212a4bb56fb70fbf` | decoded |
| Source file SHA-256 | `e576acc98325720a1cd84219906d9a9e28ba80030fec2bd6bfbc5a2d1eca5897` | computed |
| Gateway URL | `https://ipfs.io/ipfs/bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` | 🔴 gateway unreachable |

> ⚠️ **MISMATCH CONFIRMED (2026-06-09 Step 3):**  
> CID embedded SHA-256 digest ≠ Source file SHA-256.  
> This CID likely references a **different version** of the file (pre-edit, different encoding, or different content).  
> Status frozen at `mismatch_logged`. Do NOT upgrade to `verified_completed`.

---

## Chain Entry 3 — New BananaMoon NFT Metadata Candidate (Pinata, 2026-06-05)

> **Append timestamp:** 2026-06-09 (Step 3 continuation)  
> **Classification:** `bananaMoon_metadata_candidate` · Confidence: **high** · Verification: **partial**

| Field | Value | Kind |
|---|---|---|
| Filename | `bananamoon_metadata.json` | — |
| File size | 823 B | — |
| Creation date | 2026-06-05 | Pinata record date |
| Content type | NFT Metadata JSON | — |
| Pinata record | `pinata_record_found: true` | — |
| Status | `candidate_metadata_confirmed` | — |

### NFT Metadata CID

| Field | Value | Verification status |
|---|---|---|
| IPFS CID | `bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm` | 🟡 structure valid, byte-level pending |
| CID version | CIDv1 (base32 multibase, prefix `bafkrei`) | confirmed via decode |
| Multicodec | `raw` (0x55) | confirmed via decode |
| Hash function | SHA2-256 (0x12) | confirmed via decode |
| CID embedded digest | `0a8605737972c7d99ce0416efcc8d6f91d38875483620087a414479ce34346bb` | decoded |
| Gateway URL | `https://ipfs.io/ipfs/bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm` | 🔲 retrieval pending |
| Source SHA-256 | `PENDING` | raw-byte comparison not yet performed |
| Byte-level match | `PENDING` | gateway unreachable at time of append |

### Image CID (referenced by metadata)

| Field | Value | Verification status |
|---|---|---|
| IPFS CID | `bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre` | 🟡 structure valid, not retrieved |
| CID version | CIDv1 (base32 multibase) | confirmed via decode |
| Multicodec | `raw` (0x55) | confirmed via decode |
| Hash function | SHA2-256 (0x12) | confirmed via decode |
| CID embedded digest | `2e1a602d7cde426a2c2cc7004f0f06b6171c22efa951ef8a18ee5819c4660c89` | decoded |
| Gateway URL | `https://ipfs.io/ipfs/bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre` | 🔲 retrieval pending |

### Known Metadata Fields

| Field | Value | Note |
|---|---|---|
| `name` | `"BananaMoon Quantum NFT #1/1"` | — |
| `image` | references Image CID above | IPFS URI |
| Encoding | mojibake present in several fields | ⚠️ encoding reconstruction required |

> ⚠️ **Encoding Note:** Mojibake (character encoding corruption) has been observed in metadata fields.  
> Raw byte content must be reviewed for encoding (UTF-8 / UTF-16 / Shift-JIS / BOM) before treating any  
> text fields as authoritative. Encoding reconstruction is a separate pending task.

### Provenance Relationship (Entry 3)

```
BananaMoon Artwork
↓
Image CID: bafkreibodjqc27g6ijvcylghabhq6bvwc4ocf35jkhxyugholam4izqmre
↓
Metadata CID: bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm
↓
Pinata Record (2026-06-05, filename: bananamoon_metadata.json, 823 B)
↓
GitHub Provenance Documentation (this file)
↓
bananaMoon-metadata-johnson.json
↓
ipfs-provenance-chain.md
```

---

## Verification Checklist

```
[x] Compute sha256sum of raw bananaMoon-metadata-johnson.json bytes
    → integrity.sha256 = e576acc98325720a1cd84219906d9a9e28ba80030fec2bd6bfbc5a2d1eca5897
[x] CID decode: old CID (Entry 2) — mismatch confirmed, status frozen
[x] CID decode: new metadata CID (Entry 3) — structure valid (CIDv1 raw sha2-256)
[x] CID decode: image CID (Entry 3) — structure valid (CIDv1 raw sha2-256)
[ ] Retrieve Entry 3 metadata CID via gateway
    → ipfs cat bafkreiakqycxg6lsy7mzzycbn36mrvxzdu4iovedmiaipjaui6oogq2gxm
[ ] Compute SHA-256 of retrieved bytes
[ ] Compare against CID embedded digest: 0a8605737972c7d99ce0416efcc8d6f91d38875483620087a414479ce34346bb
    → Status: candidate_metadata_confirmed → verified_completed (only if match)
[ ] Retrieve Entry 3 image CID via gateway
[ ] Encoding reconstruction — review mojibake fields in bananamoon_metadata.json
[ ] Confirm Pinata pin status for both CIDs
[ ] Add verified CIDs to bananaMoon-metadata-johnson.json chain_links
```

---

## Temporal Relationship

```
2026-06-05               bananamoon_metadata.json pinned to Pinata (Entry 3 candidate)
2026-06-09T08:56:35Z     QuantumBananaMoon commit 9910fb7e  (IPFS CID Entry 2 recorded)
2026-06-09T08:58:18Z     -QACC-IYQ2025- commit 93254f9f   (provenance anchor created)
2026-06-09 (Step 3)      Entry 2 CID mismatch detected, Entry 3 candidate appended
```

---

## Repair Chain Status

| Gap | Status |
|---|---|
| G1 — `docs/` directory | `verified_completed` |
| G2 — CI deps / BananaMoon path blocker | `implemented_but_blocked` |
| G3 — QuantumChess ↔ QACC connection | `pending` |
| G4 — Spec / ReleaseStrategy layer | `pending` |
| G5 — BananaMoon Provenance chain | `step_3_partial` (Entry 3 appended, byte verification pending) |
| G6 — Supabase / Colab runtime | `pending` |

---

## Next Steps

| Step | Action | Status |
|---|---|---|
| Step 1 | Create `provenance/bananaMoon-metadata-johnson.json` anchor | ✅ `archived_original` |
| Step 2 | Create this file (`ipfs-provenance-chain.md`) | ✅ `step_2_complete` |
| Step 3a | Compute SHA-256 of Entry 1 source | ✅ `e576acc9...` |
| Step 3b | Decode all CIDs, detect Entry 2 mismatch | ✅ `mismatch_logged` |
| Step 3c | Append Entry 3 (new metadata candidate) | ✅ `candidate_metadata_confirmed` |
| Step 3d | Byte-level verify Entry 3 CID via gateway | 🔲 `pending` (gateway unreachable) |
| Step 3e | Encoding reconstruction (mojibake) | 🔲 `pending` |
| Step 4 | Create clean successor repository (no abnormal path) | 🔲 `pending` |

---

*This file is part of the CoPhelia³ × QRA v1.1 repair archaeology protocol.*  
*Do not modify chain entries retroactively. Append only.*
