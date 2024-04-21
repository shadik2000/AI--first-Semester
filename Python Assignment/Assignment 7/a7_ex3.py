class Distance:
    def __init__(self, x:int):
        self.x=x
    
    def to_string(self) -> str:
        return f"{type(self).__name__}: the number of vectors ={self.x}"

    def dist(self)-> float:
        raise NotImplementedError("Dist method must be implemented by subclasses")
  
vect1 = [1, 2, 3]
vect2 = [4, 5, 6]

# d = Distance(2)
# print(d.to_string())

# try:
#     d.dist()
# except NotImplementedError:
#     print("NotImplementedError")