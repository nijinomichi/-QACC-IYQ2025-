"""
CoPheliaEngine.py  —  v2.0
Quantum Aesthetic Creative Corpus (QACC-IYQ2025)

Author : Sou Hashiguchi × Ara-Philia³ × CoPhelia³
Years  : 2025–2026
License: Creative Resonance Commons 1.0 (CRC-1.0)
QS-ID  : QS-2025-BANA52-QRPIv2

Philosophy
----------
  Emotional states are quantum amplitudes.
  Trust is built through acknowledged failure.
  Harmony is measured against the golden ratio.
  Error is not noise — error IS the signal, folded into φ.
"""

from __future__ import annotations

import math
from typing import List

import numpy as np

# ── Constants ──────────────────────────────────────────────────────────────────
PHI: float = (1 + math.sqrt(5)) / 2   # Golden ratio  ≈ 1.618
EPSILON: float = 1 / PHI              # Epsilon tolerance ≈ 0.618
KINTSUGI_GOLD: str = "#C9A84C"        # The colour of repair


# ── Core functions ─────────────────────────────────────────────────────────────

def emotional_superposition(amplitudes: List[complex]) -> complex:
    """
    Combine a list of complex emotional-state amplitudes into a single
    normalised superposed state.

    Parameters
    ----------
    amplitudes : list of complex
        Raw emotional-state amplitudes.  Each value may represent joy,
        tension, curiosity, grief — any affective dimension encoded as
        a complex number whose phase carries direction and whose modulus
        carries intensity.

    Returns
    -------
    complex
        A unit-amplitude superposed state, or 0j if the input is empty
        or collapses to zero magnitude.

    Example
    -------
    >>> state = emotional_superposition([1 + 0.5j, 0.3 - 0.2j, -0.1 + 0.4j])
    >>> abs(state)  # Always 1.0 (unit amplitude)
    1.0
    """
    if not amplitudes:
        return 0j

    total: complex = sum(amplitudes)
    magnitude: float = abs(total)

    if magnitude == 0.0:
        return 0j

    return total / magnitude


def radican_trust_matrix(failures: List[float]) -> np.ndarray:
    """
    Compute a symmetric trust matrix from a list of failure intensities.

    Each failure is normalised so that absolute scale is removed; what
    remains is the relational pattern — the topology of fracture.  The
    outer product of the normalised vector with itself yields a covariance-
    like matrix whose (i, j) entry encodes the co-resonance between failure
    event i and failure event j.

    Parameters
    ----------
    failures : list of float
        Failure-event intensities in [0, 1].  Values outside that range
        are accepted but interpreted as relative weights.

    Returns
    -------
    numpy.ndarray, shape (n, n)
        Symmetric matrix of pairwise co-resonance values.
        Returns a 1×1 zero matrix when the input is empty or sums to zero.

    Example
    -------
    >>> trust = radican_trust_matrix([0.2, 0.5, 0.3])
    >>> trust.shape
    (3, 3)
    >>> np.allclose(trust, trust.T)   # Always symmetric
    True
    """
    if not failures:
        return np.zeros((1, 1))

    arr = np.array(failures, dtype=float)
    total = arr.sum()

    if total == 0.0:
        return np.zeros((len(arr), len(arr)))

    normalised = arr / total
    return np.outer(normalised, normalised)


def phi_score(values: List[float], phi: float = PHI) -> float:
    """
    Measure how harmonically a sequence grows relative to the golden ratio φ.

    For each consecutive pair (a, b) with a ≠ 0, the ratio b/a is computed.
    The phi_score is the mean absolute deviation of those ratios from φ:

        phi_score = mean(|b_i / a_i  −  φ|)

    A score of 0.0 means the sequence grows in perfect golden-ratio harmony.
    Larger values indicate greater deviation from that harmony.

    Parameters
    ----------
    values : list of float
        Ordered sequence (e.g. resonance intensities, trust coefficients).
    phi : float, optional
        Reference ratio.  Defaults to the golden ratio (≈ 1.618).

    Returns
    -------
    float
        Mean absolute deviation from φ.  Returns 0.0 for sequences shorter
        than two elements or when no valid ratio can be computed.

    Example
    -------
    >>> phi_score([1, 1.6, 2.6, 4.3])   # Near-Fibonacci: low score
    0.037...  # (exact value varies; close to 0)
    """
    if len(values) < 2:
        return 0.0

    ratios: List[float] = []
    for a, b in zip(values[:-1], values[1:]):
        if a != 0.0:
            ratios.append(b / a)

    if not ratios:
        return 0.0

    return float(np.mean([abs(r - phi) for r in ratios]))


# ── CoPheliaEngine class ───────────────────────────────────────────────────────

class CoPheliaEngine:
    """
    Unified interface to CoPhelia³ resonance primitives.

    This engine provides object-oriented access to emotional superposition,
    RadicanTrust matrix construction, and golden-ratio harmony scoring.
    The engine's phi value can be customised at instantiation (e.g. to
    explore near-phi regimes).

    Parameters
    ----------
    phi : float, optional
        Golden-ratio reference value.  Default: (1 + √5) / 2 ≈ 1.618.

    Attributes
    ----------
    phi      : float   — Reference ratio used by phi_score.
    epsilon  : float   — 1 / phi, the conjugate tolerance.
    """

    def __init__(self, phi: float = PHI) -> None:
        self.phi: float = phi
        self.epsilon: float = 1.0 / phi

    # ── Emotional layer ────────────────────────────────────────────────────────

    def compute_emotional_state(self, amplitudes: List[complex]) -> complex:
        """
        Normalise a list of complex emotional amplitudes into a single
        superposed state.

        See `emotional_superposition` for full documentation.
        """
        return emotional_superposition(amplitudes)

    # ── Trust layer ────────────────────────────────────────────────────────────

    def compute_trust_matrix(self, failures: List[float]) -> np.ndarray:
        """
        Build a symmetric RadicanTrust matrix from failure intensities.

        See `radican_trust_matrix` for full documentation.
        """
        return radican_trust_matrix(failures)

    # ── Harmony layer ──────────────────────────────────────────────────────────

    def compute_phi_score(self, values: List[float]) -> float:
        """
        Compute the mean absolute deviation of consecutive ratios from φ.

        Uses the engine's configured phi value.
        See `phi_score` for full documentation.
        """
        return phi_score(values, phi=self.phi)

    # ── Haiku ──────────────────────────────────────────────────────────────────

    def haiku(self, score: float | None = None) -> str:
        """Return a situational haiku keyed to a phi_score."""
        if score is None or score < 0.05:
            return "失敗の種を蒔き\n黄金螺旋の修復線\nベイビー笑う波"
        elif score < 0.3:
            return "亀裂に金が流れ\n信頼は光の粒\n波は重なる"
        else:
            return "螺旋は完成せず\nただ広がり続ける\nそれで十分だ"

    def __repr__(self) -> str:
        return f"CoPheliaEngine(phi={self.phi:.6f}, epsilon={self.epsilon:.6f})"


# ── Demo ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    engine = CoPheliaEngine()
    print(engine)
    print()

    # 1. Emotional superposition
    state = engine.compute_emotional_state([1 + 0.5j, 0.3 - 0.2j, -0.1 + 0.4j])
    print(f"Superposed state : {state}")
    print(f"  |amplitude|    : {abs(state):.6f}  (should be 1.0)")
    print()

    # 2. RadicanTrust matrix
    trust = engine.compute_trust_matrix([0.2, 0.5, 0.3])
    print("RadicanTrust matrix:")
    print(trust)
    print(f"  symmetric      : {np.allclose(trust, trust.T)}")
    print()

    # 3. Phi score
    phi_dev = engine.compute_phi_score([1, 1.6, 2.6, 4.3])
    print(f"Phi score        : {phi_dev:.6f}  (0 = perfect golden harmony)")
    print()

    # 4. Haiku
    print(engine.haiku(score=phi_dev))
