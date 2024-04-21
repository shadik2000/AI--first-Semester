# Here is an example of a generator function that generates the squares of numbers from 1 to 10:

def squares(n):
    for i in range(1, n + 1):
        yield i * i

# To use the squares() function, you would call it like this:


for square in squares(10):
    print(square)