class Computer:

    def __init__(self, cpu, ram): #It takes positional argument of class Computer constructor and assign to each object
        self.cpu= cpu   
        self.ram=ram

    # def __init__(self): #It takes positional argument of Computer constructor
    #     print("in it",self.cps, self.rams)   #for every object this will be printed

        


    def config(self): #method
        print("Config is",self.cpu, self.ram)   #for every object this will be printed



com1= Computer("i5", 16)
com2= Computer("i3", 32)



# Computer.config(com1) #it takes the positional argument as self

com1.config() #It takes self=com1
com2.config() 

