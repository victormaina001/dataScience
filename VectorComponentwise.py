def add(v, w ):
     """Adds corresponding elements"""
     assert len(v) == len(w), "vectors must be the same length"
     return [v_i + w_i for v_i, w_i in zip(v, w)]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
print(add([1, 2, 3], [4, 5, 6]))


def subtract(v, w ):
     """Subtracts corresponding elements"""
     assert len(v) == len(w), "vectors must be the same length"
     return [v_i - w_i for v_i, w_i in zip(v, w)]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
print(subtract([5, 7, 9], [4, 5, 6]))


def vector_sum(vectors):
     """Sums all corresponding elements"""
 # Check that vectors is not empty
     assert vectors, "no vectors provided!"
 # Check the vectors are all the same size
     num_elements = len(vectors[0])
     assert all(len(v) == num_elements for v in vectors), "different sizes!"
 # the i-th element of the result is the sum of every vector[i]
     return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
print(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20])

def scalar_multiply(c,v):
     """Multiplies every element by c"""
     return [c * v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
print(scalar_multiply(2, [1, 2, 3]))
def vector_mean(vectors):
    n=len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))
print(vector_mean([[1, 2], [3, 4], [5, 6]]))

def vector_mean(vectors):
     """Computes the element-wise average"""
     n = len(vectors)
     return scalar_multiply(1/n, vector_sum(vectors))
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
print(vector_mean([[1, 2], [3, 4], [5, 6]]))

#The dot product of two vectors is the sum of their componentwise products:
def dot(v,w):
     """Computes v_1 * w_1 + ... + v_n * w_n"""
     assert len(v) == len(w), "vectors must be same length"
     return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6
print(dot([1, 2, 3], [4, 5, 6]))

def sum_of_squares(v):
     """Returns v_1 * v_1 + ... + v_n * v_n"""
     return dot(v, v)
assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3
print(sum_of_squares([1, 2, 3]))

import math
def magnitude(v):
 """Returns the magnitude (or length) of v"""
 return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function
assert magnitude([3, 4]) == 5
print(magnitude([3, 4]))

def squared_distance(v,w):
     """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
     return sum_of_squares(subtract(v, w))
 
print(squared_distance[3,4])
 
def distance(v,w):
 """Computes the distance between v and w"""
 return math.sqrt(squared_distance(v, w))
