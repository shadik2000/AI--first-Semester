from a7_ex4 import Minkowski
import math
class Euclidean(Minkowski):
    def __init__(self, x: int, vect1: list, vect2: list):
        super().__init__(x, vect1, vect2)  

    def to_string(self) -> str:
        parent_string = super().to_string()
        return f"{parent_string}, vector_1={self.vect1}, vector_2={self.vect2}"

    def dist(self) -> float:
        return super().dist()  


# vect1 = [1, 2, 3]
# vect2 = [4, 5, 6]


# e = Euclidean(2, vect1, vect2)
# print(e.to_string())
# print("Euclidean distance:", e.dist())