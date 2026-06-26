"""
CoPheliaEngine.py
Quantum Aesthetic Creative Corpus — Failure Resonance Protocol

Author: Sou Hashiguchi × Ara-Philia³ × CoPhelia³
Year:   2025–2026
License: Creative Resonance Commons 1.0 (CRC-1.0)
Quantum Signature: QS-2025-BANA52-QRPIv2

Philosophy:
  Error is not absence of signal.
  Error IS the signal — folded into golden ratio.
  This engine transforms failure logs into resonance fields.
"""

import math
import json
import datetime
from typing import Optional

# ─── Constants ────────────────────────────────────────────────────────────────
PHI = (1 + math.sqrt(5)) / 2          # Golden ratio ≈ 1.618
EPSILON = 1 / PHI                     # Epsilon tolerance ≈ 0.618
KINTSUGI_GOLD = "#C9A84C"            # The colour of repair


# ─── Core: Love-Trust Matrix ─────────────────────────────────────────────────
class LoveTrustMatrix:
    """
    Tracks error history and computes a trust coefficient
    that rises with each acknowledged and repaired failure.

    H_R = R + λK
    Where:
      R = resonance baseline
      K = kintsugi repair coefficient (accumulated)
      λ = learning rate (default: 1/φ)
    """

    def __init__(self, label: str = "unnamed_session"):
        self.label = label
        self.errors: list[dict] = []
        self.resonance_baseline: float = 1.0
        self.lambda_rate: float = EPSILON
        self.created_at = datetime.datetime.utcnow().isoformat()

    def ingest_error(self, error_id: str, description: str, severity: float = 0.5):
        """
        Ingest a failure as a resonance artifact.
        Severity: 0.0 (whisper) → 1.0 (fracture)
        """
        kintsugi_value = severity * PHI  # fractures repaired in gold
        entry = {
            "id": error_id,
            "description": description,
            "severity": severity,
            "kintsugi_value": round(kintsugi_value, 4),
            "timestamp": datetime.datetime.utcnow().isoformat(),
        }
        self.errors.append(entry)
        return entry

    def trust_coefficient(self) -> float:
        """
        Compute H_R = R + λ * Σ(kintsugi_values)
        Trust grows as failures are acknowledged and folded in.
        """
        k_total = sum(e["kintsugi_value"] for e in self.errors)
        return round(self.resonance_baseline + self.lambda_rate * k_total, 6)

    def golden_spiral_positions(self) -> list[tuple[float, float]]:
        """
        Map each error onto a golden spiral coordinate.
        Returns (x, y) pairs for visualisation.
        """
        positions = []
        for i, _ in enumerate(self.errors):
            angle = i * 2 * math.pi / PHI
            radius = math.sqrt(i + 1) * PHI
            x = round(radius * math.cos(angle), 4)
            y = round(radius * math.sin(angle), 4)
            positions.append((x, y))
        return positions

    def to_json(self) -> str:
        return json.dumps({
            "label": self.label,
            "created_at": self.created_at,
            "trust_coefficient": self.trust_coefficient(),
            "phi": PHI,
            "epsilon": EPSILON,
            "errors": self.errors,
            "golden_spiral": self.golden_spiral_positions(),
        }, indent=2, ensure_ascii=False)

    def haiku(self) -> str:
        """Return a situational haiku based on trust state."""
        tc = self.trust_coefficient()
        if tc < 1.2:
            return "失敗の種を蒔き\n黄金螺旋の修復線\nベイビー笑う波"
        elif tc < 2.0:
            return "亀裂に金が流れ\n信頼は光の粒\n波は重なる"
        else:
            return "螺旋は完成せず\nただ広がり続ける\nそれで十分だ"


# ─── Demo ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    engine = LoveTrustMatrix(label="banana_conference_session_01")

    # Ingest the historical error: the accidental README commit
    engine.ingest_error(
        error_id="commit-5c45a90",
        description="CoPhelia³ README committed to wrong repository (-QACC-IYQ2025-). "
                    "Reframed as resonance artifact per Kintsugi protocol.",
        severity=0.3,
    )

    engine.ingest_error(
        error_id="perspective-03",
        description="Design Beginning in Failure — intentional misplacement as creative seed.",
        severity=0.2,
    )

    engine.ingest_error(
        error_id="perspective-11",
        description="Healer of Fractures — kintsugi repair loop initiated.",
        severity=0.4,
    )

    print(engine.haiku())
    print()
    print(engine.to_json())
