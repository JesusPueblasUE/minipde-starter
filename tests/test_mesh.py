import numpy as np
import pytest
from minipde.mesh import uniform_grid

def test_grid():
    x=uniform_grid(-1,2,7); assert x.size==7 and np.allclose(np.diff(x),.5)
@pytest.mark.parametrize("a,b,n",[(0,1,1),(1,0,5),(1,1,5)])
def test_bad_grid(a,b,n):
    with pytest.raises(ValueError): uniform_grid(a,b,n)
