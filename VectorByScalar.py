from VectorComponentwise import vector_sum
def scalar_multiply(c,v):
     """Multiplies every element by c"""
     return [c * v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
print(scalar_multiply(2, [1, 2, 3]))