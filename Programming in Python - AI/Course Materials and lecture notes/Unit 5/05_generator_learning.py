

#The function to be generator it must use a keyword 'yield'

# def myfunc():
#     yield 6
#     yield 5
#     yield 4
#     yield 3


#print(myfunc()) #<generator object myfunc at 0x000002910A921700>

# output = myfunc()

# for item in output:
#     print(item)
#     print("\n")

# #OR

# for item in myfunc():
#     print(item)

# print(output.__next__()) #6
# print(output.__next__()) #6 5
# print(output.__next__()) #6 5 4



def myfunc():
    n=1

    while n<=10:
        op = 2*n + 1
        yield op #return will terminate the function but yield will not
        n += 1

for item in myfunc():
    print(item)

