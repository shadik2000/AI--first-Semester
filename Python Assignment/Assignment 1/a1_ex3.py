# Taking user input of length, width and height

l=float(input("Length (meters): "))
b=float(input("Width (meters): "))
h=float(input("Height (meters): "))


#The circumference of the room (float)

circumference=2*(l+b)
print("Circumference:", circumference, "meters")

# The volume of the room (float)

volume=l*b*h
print("Volume:", volume, "cubic meters")

#The wall area of the room, i.e., the four side walls (float)

area_of_wall=2*h*(l+b)
print("Wall area:", area_of_wall, "square meters")

#The number of required windows (int)

area_of_wall=2*h*(l+b)
windows=area_of_wall//12
print("Number of windows:",windows )

#The amount of paint that is needed to paint the walls (float)

area_of_wall_without_window=2*h*(l+b)-windows*2
required_paints=0.75*area_of_wall_without_window
print("Needed paint:",required_paints,"liters")


