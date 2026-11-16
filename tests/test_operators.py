import numpy as np
import pytest
from minipde import uniform_grid, first_derivative, second_derivative

def test_polynomials():
    x=uniform_grid(-1,1,21)
    assert np.allclose(first_derivative(x,2*x-1),2)
    assert np.allclose(second_derivative(x,x*x),2,atol=1e-12)
def test_order_two():
    errors=[]
    for n in (41,81,161):
        x=uniform_grid(0,2*np.pi,n); errors.append(np.max(np.abs(first_derivative(x,np.sin(x))-np.cos(x))))
    assert np.all(np.log2(np.array(errors[:-1])/errors[1:])>1.8)
def test_nonuniform():
    x=np.array([0,.2,.5,1.])
    with pytest.raises(ValueError): first_derivative(x,x)
