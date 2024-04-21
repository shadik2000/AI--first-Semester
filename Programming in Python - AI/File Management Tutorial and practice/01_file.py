#Reading and writing from file
"""Open a file in read mode"""

# with open('example.txt', 'r') as file:
#     content = file.read(10)
#     print(content)

# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line)

# with open('example.txt', 'r') as file:
#     for line in file:
#         with open('output.txt', 'w') as file:
#             file.write(line)

"""Opening a file in writing mode"""  
with open('output.txt', 'w') as file:
    file.write("Hello, this is a sample text.")
