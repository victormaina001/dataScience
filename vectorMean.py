from VectorByScalar import scalar_multiply
from VectorComponentwise import vector_sum
def vector_mean(vectors):
    n=len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))
print(vector_mean([[1, 2], [3, 4], [5, 6]]))