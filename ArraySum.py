import math
li = [1,2,3,4]
from functools import reduce
print(reduce(lambda x,y : x+y,li))

from operator import add
from itertools import accumulate
print(list(accumulate(li,add))[-1])



def summation(li):
    val = 0
    for i in li:
        val += i
    return val
print(summation(li))