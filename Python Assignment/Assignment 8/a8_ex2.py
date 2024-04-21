
class Power:
    def __init__(self, exponent):
        if not isinstance(exponent, (int, float)):
            raise TypeError("The exponent must be a numerical value.")
        self.exponent = exponent


    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a numerical value.")

        else:
            return x**self.exponent
        
    def __mul__(self, other):
        
        if isinstance(other, (int, float)):
            return Power(self.exponent + other)
        elif isinstance(other, Power):
            return Power(self.exponent + other.exponent)
        else:
            return NotImplemented

class Square(Power):
    def __inti__(self):
        super().__init__(2)


x = 3
square = Square(2)
cube = Power(3)
print(square.exponent, square(x))
print(cube.exponent, cube(x))
m1 = square *2
print(m1.exponent, m1.__call__(x))
m2 = square *cube
print(m2.exponent, m2.__call__(x))


try :
    Square("foo")
except TypeError as e:
    print(e)
try :
    Power("foo")
except TypeError as e:
    print(e)


