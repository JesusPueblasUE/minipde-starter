import numpy as np
from minipde import uniform_grid, solve_poisson_1d, max_error, observed_order

def source(x): return np.pi**2*np.sin(np.pi*x)
sizes=(21,41,81,161); hs=[]; errors=[]
for n in sizes:
    x=uniform_grid(0,1,n); hs.append(x[1]-x[0]); errors.append(max_error(solve_poisson_1d(x,source),np.sin(np.pi*x)))
orders=observed_order(hs,errors)
print("N,h,error,order")
for i,n in enumerate(sizes): print(n,hs[i],errors[i],"-" if i==0 else orders[i-1])
