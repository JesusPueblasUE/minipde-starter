"""Dense educational solver for -u''=f with Dirichlet conditions."""
import numpy as np

def _grid(x):
    x=np.asarray(x,float)
    if x.ndim!=1 or x.size<3 or not np.all(np.isfinite(x)): raise ValueError("invalid grid")
    dx=np.diff(x)
    if np.any(dx<=0) or not np.allclose(dx,dx[0],rtol=1e-12,atol=1e-14): raise ValueError("uniform grid required")
    return x,float(dx[0])

def assemble_poisson_1d(x, source, left=0.0, right=0.0):
    x,h=_grid(x); f=np.asarray(source(x),float)
    if f.shape!=x.shape or not np.all(np.isfinite(f)): raise ValueError("source(x) must match x")
    n=x.size; A=np.zeros((n,n)); b=np.zeros(n); A[0,0]=A[-1,-1]=1; b[0]=left; b[-1]=right
    i=np.arange(1,n-1); A[i,i-1]=-1; A[i,i]=2; A[i,i+1]=-1; b[1:-1]=h*h*f[1:-1]
    return A,b

def solve_poisson_1d(x, source, left=0.0, right=0.0):
    A,b=assemble_poisson_1d(x,source,left,right); return np.linalg.solve(A,b)

def residual_norm(A,u,b):
    return float(np.linalg.norm(np.asarray(A)@np.asarray(u)-np.asarray(b),ord=np.inf))
