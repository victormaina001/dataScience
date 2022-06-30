
from VectorComponentwise import dot, subtract
def sum_of_squares(v):
     """Returns v_1 * v_1 + ... + v_n * v_n"""
     return dot(v, v)

import math
def magnitude(v):
 """Returns the magnitude (or length) of v"""
 return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function

def squared_distance(v,w):
     """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
     return sum_of_squares(subtract(v, w))
 
print(squared_distance([4, 5, 6],[1, 2, 3]))