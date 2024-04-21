str_part=input("Enter comma-separated elements: ")

comma_separated=str_part.split(',')

integers=[]
rest=[]
counts={}

for string_part in comma_separated:
    if string_part.isdecimal():
        string_part=int(string_part)
        integers.append(string_part)

    else:
        rest.append(string_part)


for num in integers:
    count_of_integers=integers.count(num)
    counts[num]=count_of_integers


print("integers:",integers)
print("counts:",counts)
print("rest:",rest)

