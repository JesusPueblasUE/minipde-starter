import numpy as np
import pytest
from minipde import uniform_grid, assemble_poisson_1d, solve_poisson_1d, residual_norm

def source(x): return np.pi**2*np.sin(np.pi*x)
def test_boundaries():
    x=uniform_grid(0,1,21); u=solve_poisson_1d(x,source,1.25,-.5)
    assert u[0]==pytest.approx(1.25) and u[-1]==pytest.approx(-.5)
def test_order_two():
    e=[]
    for n in (21,41,81):
        x=uniform_grid(0,1,n); e.append(np.max(np.abs(solve_poisson_1d(x,source)-np.sin(np.pi*x))))
    assert np.all(np.log2(np.array(e[:-1])/e[1:])>1.8)
def test_residual():
    x=uniform_grid(0,1,41); A,b=assemble_poisson_1d(x,source); u=np.linalg.solve(A,b)
    assert residual_norm(A,u,b)<1e-12
