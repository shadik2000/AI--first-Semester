class Computers:

    def __init__(self): 
        self.name="acer"
        self.num=6789


    def update(self):
        self.name="dell"

    def compare(self, other):
        return self.name == other.name


com1= Computers()
com2= Computers()




# print(com1.name) #acer
# print(com2.name) #acer

##can change name
# com1.name="hp"

# com1.update() #dell

print(com1.compare(com2)) #true if not updated


# print(com1.name) #hp
