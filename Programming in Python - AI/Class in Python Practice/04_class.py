"""Methods in Class"""

class Student :

    uni = "JKU"

    def __init__(self, m1, m2, m3):
        self.m1 =m1
        self.m2 =m2
        self.m3 =m3

    def avg(self):
        return (self.m1+ self.m2+self.m3)/3
    
    
    @classmethod
    def getSchool(cls):
        return cls.uni
    
    @staticmethod
    def info():
        print("This is student class")


s1 =Student(2,3,4)
s2 =Student(4,6,7)

# print(s1.avg()) #3.0

# print(s1.info()) #JKU
# print(Student.getSchool()) #JKU
# Student.info() #don't have to pass anything not even object or anything 
                #Output = This is student class

