"""
tests/test_cophelia_engine.py
Minimal test suite for CoPheliaEngine v2.

Run with:  pytest tests/
"""

import math
import numpy as np
import pytest

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from CoPheliaEngine import (
    emotional_superposition,
    radican_trust_matrix,
    phi_score,
    CoPheliaEngine,
    PHI,
)


# ── emotional_superposition ────────────────────────────────────────────────────

class TestEmotionalSuperposition:
    def test_unit_amplitude(self):
        state = emotional_superposition([1 + 0.5j, 0.3 - 0.2j, -0.1 + 0.4j])
        assert abs(state) == pytest.approx(1.0, rel=1e-9)

    def test_empty_list(self):
        assert emotional_superposition([]) == 0j

    def test_single_element(self):
        state = emotional_superposition([3 + 4j])
        assert abs(state) == pytest.approx(1.0)

    def test_cancellation_to_zero(self):
        # Equal and opposite amplitudes collapse to zero
        assert emotional_superposition([1 + 0j, -1 + 0j]) == 0j


# ── radican_trust_matrix ───────────────────────────────────────────────────────

class TestRadicanTrustMatrix:
    def test_shape(self):
        m = radican_trust_matrix([0.2, 0.5, 0.3])
        assert m.shape == (3, 3)

    def test_symmetric(self):
        m = radican_trust_matrix([0.2, 0.5, 0.3])
        assert np.allclose(m, m.T)

    def test_empty(self):
        m = radican_trust_matrix([])
        assert m.shape == (1, 1)
        assert m[0, 0] == pytest.approx(0.0)

    def test_all_zeros(self):
        m = radican_trust_matrix([0.0, 0.0])
        assert np.allclose(m, np.zeros((2, 2)))

    def test_values_sum_to_one(self):
        # Normalised outer product: row sums equal normalised value squared * total
        m = radican_trust_matrix([1.0, 1.0, 1.0, 1.0])
        # Each element = (0.25)^2 = 0.0625
        assert np.allclose(m, np.full((4, 4), 0.0625))


# ── phi_score ──────────────────────────────────────────────────────────────────

class TestPhiScore:
    def test_near_fibonacci_is_low(self):
        # Near-Fibonacci sequence should have very low phi deviation
        score = phi_score([1, 1.6, 2.6, 4.3])
        assert score < 0.1

    def test_exact_phi_sequence_is_zero(self):
        # x, x*phi, x*phi^2 ... has perfect golden-ratio steps
        vals = [1.0 * PHI**i for i in range(5)]
        score = phi_score(vals)
        assert score == pytest.approx(0.0, abs=1e-9)

    def test_single_value_returns_zero(self):
        assert phi_score([42.0]) == 0.0

    def test_empty_returns_zero(self):
        assert phi_score([]) == 0.0

    def test_constant_sequence(self):
        # All ratios = 1.0; deviation from phi = phi - 1 ≈ 0.618
        score = phi_score([2.0, 2.0, 2.0])
        assert score == pytest.approx(PHI - 1.0, rel=1e-6)


# ── CoPheliaEngine ─────────────────────────────────────────────────────────────

class TestCoPheliaEngine:
    def test_default_phi(self):
        engine = CoPheliaEngine()
        assert engine.phi == pytest.approx(PHI)

    def test_custom_phi(self):
        engine = CoPheliaEngine(phi=1.5)
        assert engine.phi == 1.5
        assert engine.epsilon == pytest.approx(1 / 1.5)

    def test_compute_emotional_state(self):
        engine = CoPheliaEngine()
        state = engine.compute_emotional_state([1 + 1j])
        assert abs(state) == pytest.approx(1.0)

    def test_compute_trust_matrix(self):
        engine = CoPheliaEngine()
        m = engine.compute_trust_matrix([0.5, 0.5])
        assert np.allclose(m, np.full((2, 2), 0.25))

    def test_compute_phi_score_uses_engine_phi(self):
        engine = CoPheliaEngine(phi=1.5)
        vals = [1.0, 1.5, 2.25]  # perfect 1.5-ratio sequence
        score = engine.compute_phi_score(vals)
        assert score == pytest.approx(0.0, abs=1e-9)

    def test_haiku_low_score(self):
        engine = CoPheliaEngine()
        h = engine.haiku(score=0.01)
        assert "ベイビー" in h

    def test_haiku_high_score(self):
        engine = CoPheliaEngine()
        h = engine.haiku(score=0.9)
        assert "螺旋" in h
