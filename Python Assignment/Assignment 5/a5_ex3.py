def gen_fibonacci(upper_bound):
    if not isinstance(upper_bound, (int, float)):
        raise TypeError("Upper bound should be either integer or float")
    
    if upper_bound < 0:
        raise ValueError("Upper bound must be non-negative")

    a, b = 0, 1
    while a <= upper_bound:
        yield a
        a, b = b, a + b

# Example function calls
try:
    print(list(gen_fibonacci("3")))
except TypeError as e:
    print(e)

try:
    print(list(gen_fibonacci(-1)))
except ValueError as e:
    print(e)

# print(list(gen_fibonacci(0)))
# # Output: [0]

# print(list(gen_fibonacci(1)))
# # Output: [0, 1, 1]

# print(list(gen_fibonacci(3)))
# # Output: [0, 1, 1, 2, 3]

# print(list(gen_fibonacci(9.2)))
# # Output: [0, 1, 1, 2, 3, 5, 8]
