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
| `integrity.sha256` | `PENDING` | Raw-file SHA-256 — not yet computed |
| Commit timestamp | 2026-06-09T08:58:18Z | UTC |
| Commit author | `nijinomichi` | — |
| Status | `archived_original` | — |

> **Note on SHA types:** `commit.sha` is a Git commit SHA-1. `blob.sha` is a Git blob SHA-1  
> computed as `SHA1("blob {size}\0{content}")` — it is **not** a SHA-256 digest of raw file bytes.  
> The `integrity.sha256` field above must be populated via `sha256sum` on the raw file before IPFS/CID cross-verification can proceed.

---

## Chain Entry 2 — IPFS / Pinata Record (`QuantumBananaMoon`)

| Field | Value | Kind |
|---|---|---|
| Repository | [`nijinomichi/QuantumBananaMoon`](https://github.com/nijinomichi/QuantumBananaMoon) | — |
| File path | `provenance/bananaMoon-metadata-johnson.json` | — |
| Commit SHA | `9910fb7eeb242857d53bc004454e096f18a8fc58` | Git commit SHA-1 |
| Commit timestamp | 2026-06-09T08:56:35Z | UTC |
| Files changed | `provenance/bananaMoon-metadata-johnson.json` (+99 lines) | — |
| Commit author | `nijinomichi` | — |
| Status | `implemented_but_not_verified` | — |

### IPFS / Pinata Reference

| Field | Value | Verification status |
|---|---|---|
| Pinata File ID | `019e97c3-6e28-7fd8-907c-63660840fc25` | 🟡 present, not independently verified |
| IPFS CID | `bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` | 🟡 present, not independently verified |
| CID version | CIDv1 (inferred from `bafkrei` prefix — base32 multibase) | inferred |
| Multicodec | `raw` (inferred) | inferred |
| Hash function | SHA2-256 (standard Pinata default) | inferred |
| Gateway URL | `https://ipfs.io/ipfs/bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4` | 🔲 retrieval not attempted |

> ⚠️ The IPFS CID listed above has **not** been independently retrieved or byte-level verified.  
> Verification requires: `ipfs cat <CID>` or gateway fetch + SHA-256 comparison against source file.

### Source File Reference

| Field | Value | Kind |
|---|---|---|
| Source filename | `bananamoon_nft_metadata_1763131775250.json` | — |
| Source path | `attached_assets/bananamoon_nft_metadata_1763131775250.json` | — |
| Source SHA | `283acb9a2d1fc80ebcb19d90226f9a37882c6735` | Git blob SHA-1 (≠ SHA-256) |
| Source SHA-256 | `PENDING` | Raw-file SHA-256 — not yet computed |
| Source status | Referenced in commit message; file deleted from repo | — |

---

## Verification Checklist

```
[ ] Compute sha256sum of raw bananaMoon-metadata-johnson.json bytes
    → Populate integrity.sha256 in Chain Entry 1
[ ] Compute sha256sum of raw bananamoon_nft_metadata_1763131775250.json bytes
    → Populate source SHA-256 in Chain Entry 2
[ ] Retrieve IPFS CID via gateway or local node
    → ipfs cat bafkreigkqm5jqmnyabnm37txp4igbafravs2urbdrqlbaijkjo2w7nypx4
[ ] Compare retrieved bytes against source SHA-256
    → Status: implemented_but_not_verified → verified_completed
[ ] Confirm Pinata File ID 019e97c3-6e28-7fd8-907c-63660840fc25 is still pinned
[ ] Add verified CID to bananaMoon-metadata-johnson.json chain_links[1]
```

---

## Temporal Relationship

```
2026-06-09T08:56:35Z  QuantumBananaMoon commit 9910fb7e  (IPFS CID recorded)
2026-06-09T08:58:18Z  -QACC-IYQ2025- commit 93254f9f   (provenance anchor created)
                       ↑ 1m 43s gap — parallel execution on same day
```

Both entries were created within the same automated CoPhelia³ session.  
Neither has been independently verified post-creation.

---

## Repair Chain Status

| Gap | Status |
|---|---|
| G1 — `docs/` directory | `verified_completed` |
| G2 — CI deps / BananaMoon path blocker | `implemented_but_blocked` |
| G3 — QuantumChess ↔ QACC connection | `pending` |
| G4 — Spec / ReleaseStrategy layer | `pending` |
| G5 — BananaMoon Provenance chain | `step_2_complete` (Step 2 of 4) |
| G6 — Supabase / Colab runtime | `pending` |

---

## Next Steps

| Step | Action | Status |
|---|---|---|
| Step 1 | Create `provenance/bananaMoon-metadata-johnson.json` anchor | ✅ `archived_original` |
| Step 2 | Create this file (`ipfs-provenance-chain.md`) | ✅ `step_2_complete` |
| Step 3 | Compute SHA-256 digests + verify IPFS CID retrieval | 🔲 `pending` |
| Step 4 | Create clean successor repository (no abnormal path) | 🔲 `pending` |

---

*This file is part of the CoPhelia³ × QRA v1.1 repair archaeology protocol.*  
*Do not modify chain entries retroactively. Append only.*
