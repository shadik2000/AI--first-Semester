import numpy as np


# zeros_array = np.zeros((5))
# ones_array = np.ones((2,3))
# range_array = np.arange(0, 10, 2)


# print(ones_array)
# print(zeros_array)
# print(range_array)



# arr = np.array([[1, 2, 3], [4, 5, 6]])

# # Accessing elements by index
# print(arr[0, 1])   # Output: 2

# # Slicing a 2D array
# print(arr[:, 1:])  # Output: [[2, 3], [5, 6]]


arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to a 2D array
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack arrays vertically
vertical_stack = np.vstack((a, b))

# Stack arrays horizontally
horizontal_stack = np.hstack((a, b))

# Split an array
split_arr = np.split(reshaped_arr, 2, axis=0)


# print(vertical_stack)
# print(horizontal_stack)


# Generating random numbers
random_array = np.random.rand(3, 3)

# Generating random integers
random_integers = np.random.randint(1, 10, size=(2, 3))

print(random_array)