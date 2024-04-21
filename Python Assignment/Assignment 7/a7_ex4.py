from a7_ex3 import Distance

class Minkowski(Distance):
    def  __init__(self, x: int, vect1: list, vect2:list):
        super().__init__(x) 
        self.vect1=vect1
        self.vect2=vect2

    def to_string(self) -> str:
        parent_string = super().to_string()
        return f"{parent_string}, vector_1={self.vect1}, vector_2={self.vect2}"
    
    def dist(self) -> float:
        if len(self.vect1) != len(self.vect2):
            raise ValueError("Vectors must have the same length")

        p = 2  # Minkowski distance with p=2
        minkowski_distance = (sum(max(v1 - v2, v2 - v1) ** p for v1, v2 in zip(self.vect1, self.vect2)) ** (1 / p))
        return float("{:.4f}".format(minkowski_distance))

vect1 = [1, 2, 3]
vect2 = [4, 5, 6]

# k = Minkowski(2, vect1, vect2)
# print(k.to_string())
# print("Minkowski distance: ", k.dist())


# Minkowski: the number of vectors =2, vector_1=[1, 2, 3], vector_2=[4, 5, 6]
# Minkowski distance: 5.1962