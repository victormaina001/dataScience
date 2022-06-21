from timeit import timeit
import numpy as np
import timeit
B = np.random.rand(1000000)
%timeit sum(B)
%timeit np.sum(B)  # B.sum()
def mySum(G):
    s = 0
    for x in G:
        s+=x
    return s

