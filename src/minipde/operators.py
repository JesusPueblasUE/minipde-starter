"""Second-order finite-difference operators on uniform 1D grids."""
import numpy as np

def _data(x, u, minimum):
    x, u = np.asarray(x, float), np.asarray(u, float)
    if x.ndim != 1 or u.ndim != 1 or x.shape != u.shape or x.size < minimum:
        raise ValueError("incompatible one-dimensional data")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(u)):
        raise ValueError("data must be finite")
    dx = np.diff(x)
    if np.any(dx <= 0) or not np.allclose(dx, dx[0], rtol=1e-12, atol=1e-14):
        raise ValueError("a strictly increasing uniform grid is required")
    return u, float(dx[0])

def first_derivative(x, u):
    u, h = _data(x, u, 3); out = np.empty_like(u)
    out[1:-1] = (u[2:] - u[:-2]) / (2*h)
    out[0] = (-3*u[0] + 4*u[1] - u[2]) / (2*h)
    out[-1] = (3*u[-1] - 4*u[-2] + u[-3]) / (2*h)
    return out

def second_derivative(x, u):
    u, h = _data(x, u, 4); out = np.empty_like(u); h2 = h*h
    out[1:-1] = (u[:-2] - 2*u[1:-1] + u[2:]) / h2
    out[0] = (2*u[0] - 5*u[1] + 4*u[2] - u[3]) / h2
    out[-1] = (2*u[-1] - 5*u[-2] + 4*u[-3] - u[-4]) / h2
    return out
