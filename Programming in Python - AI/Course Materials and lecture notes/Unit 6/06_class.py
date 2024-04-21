"""Inheritance"""


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("f1")

    def feature2(self):
        print("f2")


# class C:
#     def feature5(self):
#         print("f5")

#     def feature6(self):
#         print("f6")

class B(A):
    def __init__(self):
        super().__init__() #call init of both B and A
        print("in B init")

    def feature3(self):
        print("f3")

    def feature4(self):
        print("f4")

#Class C can access methods of B and then A as B can access A
# class C(B):
#     def feature5(self):
#         print("f5")

#     def feature6(self):
#         print("f6")


# a1 =A()

b1=B()

print(b1) #It will print init of B other wise search in A  ps. b1 inherits methods of both B and A
# c1=C()

# a1.feature1()
