def generate_range(n):
    i = 0
    while i < n:
     yield i # every call to yield produces a value of the generator
     i += 1
     
for i in generate_range(10):
 print(f"i: {i}")