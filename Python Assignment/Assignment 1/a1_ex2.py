#Taking integer input from the console
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))

#The sum of a, b and d
sum = a+b+d
print("Sum of a, b and d: ", sum)

#Product of all four numbers5

product=a*b*c*d
print("Product of all numbers:", product)

print("The sum of a and b times the sum of c and d:", (a+b)*(c+d))

#The result of an integer division when dividing a by d
print("a divided by d (int):", a//d)

#The result of a regular division when dividing a by d
print("a divided by d (float):", a/d)

#The remainder of a division (modulo) when dividing a by b
print("Remainder of a divided by b:", a%b)

#c^-a
print("c to the power of-a:", c ** -a)

#b^1/2
print("b to the power of 1/2 (square root):", b ** 0.5)

#Complex equation
complex_equation=(b/3)*(b**(a+0.5*d)-1) + c
print("Complex equation:", complex_equation)