import math 
ls = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    ls.append(ele)

print(n) 
result=math.fsum(ls)
print(result)