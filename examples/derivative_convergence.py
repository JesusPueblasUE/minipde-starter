import numpy as np
from minipde import uniform_grid, first_derivative, second_derivative, max_error, observed_order
sizes=(21,41,81,161,321); hs=[]; e1=[]; e2=[]
for n in sizes:
    x=uniform_grid(0,2*np.pi,n); u=np.sin(x); hs.append(x[1]-x[0])
    e1.append(max_error(first_derivative(x,u),np.cos(x)))
    e2.append(max_error(second_derivative(x,u),-np.sin(x)))
p1=observed_order(hs,e1); p2=observed_order(hs,e2)
print("N,h,E1,p1,E2,p2")
for i,n in enumerate(sizes): print(n,hs[i],e1[i],"-" if i==0 else p1[i-1],e2[i],"-" if i==0 else p2[i-1])