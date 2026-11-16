"""One-dimensional mesh utilities."""
import numpy as np

def uniform_grid(a: float, b: float, n: int) -> np.ndarray:
    if isinstance(n, bool) or not isinstance(n, (int, np.integer)):
        raise TypeError("n must be an integer")
    if n < 2 or not np.isfinite(a) or not np.isfinite(b) or b <= a:
        raise ValueError("require finite a < b and n >= 2")
    return np.linspace(a, b, n, dtype=float)