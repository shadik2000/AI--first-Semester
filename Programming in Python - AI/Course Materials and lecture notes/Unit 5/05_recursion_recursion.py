# def mat(n):
#     if n == 0:
#         return []
    
#     return [n] + mat(n - 1) #[8, 7, 6, 5, 4, 3, 2, 1]
    
#     return mat(n - 1) + [n] #[1, 2, 3, 4, 5, 6, 7, 8]



# hello = mat(8)
# print(hello)


def fibonacci(n):
    # Base cases:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Recursive case:
    # For n greater than 2, compute the Fibonacci sequence recursively.
    fib_sequence = fibonacci(n - 1)

    # Append the sum of the last two elements of the sequence to the sequence itself.
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Test the function:
print(fibonacci(10))
