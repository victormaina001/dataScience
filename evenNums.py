def generate_range(n):
    i = 0
    while i < n:
     yield i # every call to yield produces a value of the generator
     i += 1
data =  (i for i in generate_range(20) if i % 2 == 0)
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

print(data)

