#Creating four variables of different data types that is bool, int, float and str

bool_var=True           #bool data type
integer_var=10             #int data type
float_var=66320.8987        #float data type
string_var="hello"   #string datatype


print(bool_var)

#printing integer with minimum width of 5 with leading zeros
print( f"{integer_var:05d}")

#float with a minimu width of 10 and decimals precision is 3
print(f"Float Variable is {float_var:010.3f}") 

#String will be printed 3 times
print(string_var*3)

    