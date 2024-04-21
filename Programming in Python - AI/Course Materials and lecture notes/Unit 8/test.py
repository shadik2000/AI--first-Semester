class Fraction:
    
    def __init__(self, numerator: int, denominator: int):
        self.n = numerator
        self.d = denominator
    
    #
    # Task 1
    #
    
    # Extend the "Fraction" class by providing the special method "__eq__" to
    # enable equality checks on "Fraction" objects. A "Fraction" should be
    # considered equal to another "Fraction" if and only if they have the same
    # numerators and denominators, i.e., fractions such as 1/2 and 2/4 are not
    # considered equal. Specification:
    # https://docs.python.org/3/reference/datamodel.html#object.__eq__
    def __eq__(self, other):
        
        if isinstance(other, Fraction):
            return other.n == self.n and self.d and self.d == other.d
        
        return NotImplemented
    
    def __str__(self):
        return f"{self.n}/{self.d}"
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            return (self.n*other.d + other.n*self.d), (self.d * other.d)
    
        if isinstance(other, int):
            return (self.n + other*self.d), (self.d)
        return NotImplemented
        

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.n * other.n, self.d*other.d)
        if isinstance(other, int):
            return Fraction(self.n * other, self.d)
        
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Fraction):
            self.n = self.n*other.d + other.n*self.d
            self.d = self.d*other.d 
            
            return self
    
        if isinstance(other, int):
            self.n = self.n + other*self.d
            return self
        
        return NotImplemented
    
"""Equality"""
f1=Fraction(1,2)
f2=Fraction(2,4)
# f3=Fraction(1,2)
# print(f1==f2)
"""String"""

# f1=Fraction(1,2)
# print(str(f1))


"""ADD"""
# print(f1+f2)
# print(f1+10)


"""Multiply"""
# print(f1*10)
# print(f1*f2)
# print(str(f1*f2))

"""iADD"""
print(f1)

