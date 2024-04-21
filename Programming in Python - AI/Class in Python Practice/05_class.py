"""class inside class"""

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() #Accesing Laptop class by object

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


s1 = Student("Maria", 45)
s2 = Student("Nausheen", 4)

# print(s2.lap.brand) #HP

s2.lap.brand = "Acer" #Updating laptop brand for s2

# print(s2.lap.brand) #Acer

s1.show() #Maria 45
            #HP 8