"""Tests for floating-point examples."""

import math

import pytest

from minipde.floating_point import (
    direct_sqrt_increment,
    stable_sqrt_increment,
)


def test_direct_expression_for_moderate_increment() -> None:
    """The direct formula must work for a moderate increment."""
    x = 1.0e-4
    expected = math.sqrt(1.0 + x) - 1.0

    result = direct_sqrt_increment(x)

    assert result == pytest.approx(expected)


def test_stable_expression_for_moderate_increment() -> None:
    """Direct and stable formulas must agree for a moderate value."""
    x = 1.0e-4

    direct = direct_sqrt_increment(x)
    stable = stable_sqrt_increment(x)

    assert stable == pytest.approx(direct, rel=1.0e-10)


def test_stable_expression_preserves_small_increment() -> None:
    """The stable expression must preserve a very small increment."""
    x = 1.0e-16
    expected = x / (math.sqrt(1.0 + x) + 1.0)

    result = stable_sqrt_increment(x)

    assert result == pytest.approx(expected)
    assert result > 0.0