class Car:
    #wheels is class variable
    wheels = 4

    def __init__(self): #all the varibles inside init is instance variable
        self.mileage=90 #instance variables :it can be changed
        self.company ="Audi"


c1 = Car()
c2 = Car()

#instance variable mileage being changed
c1.mileage= 80 

print(c1.company, c1.mileage, c1.wheels) #Audi 80 4
print(c2.company, c2.mileage, c2.wheels) #Audi 80 4

#change class variable by using class namespace
Car.wheels =8 

print(c1.company, c1.mileage, c1.wheels) #Audi 80 8
print(c2.company, c2.mileage, c2.wheels) #Audi 80 8
