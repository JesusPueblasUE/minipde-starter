"""Examples illustrating floating-point stability."""

from __future__ import annotations

import math


def direct_sqrt_increment(x: float) -> float:
    """Evaluate sqrt(1 + x) - 1 directly.

    Parameters
    ----------
    x
        Increment added to one.

    Returns
    -------
    float
        Direct floating-point evaluation.

    Notes
    -----
    For sufficiently small positive values of ``x``, this expression
    suffers from catastrophic cancellation.
    """
    return math.sqrt(1.0 + x) - 1.0


def stable_sqrt_increment(x: float) -> float:
    """Evaluate sqrt(1 + x) - 1 using a stable expression.

    Parameters
    ----------
    x
        Increment added to one.

    Returns
    -------
    float
        Numerically stable evaluation.
    """
    return x / (math.sqrt(1.0 + x) + 1.0)