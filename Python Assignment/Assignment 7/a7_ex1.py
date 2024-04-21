import math

class Radian:

    def __init__(self, degree:float):
        self.degree=degree

    def rad(self) -> float:
        return f"{self.degree * (math.pi/180.0):.2f}"
    
    
    def print(self):
        print(f"The degree is {self.degree:.2f} and the radian is {self.rad()}")


c= Radian(120)
print(c.rad()) 
c.print()   
        