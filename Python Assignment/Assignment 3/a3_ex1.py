
rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))


print(" "*3,end='')

#printing column number
for i in range(cols):
    if i==cols-1:
        print(i,end='')
        print()

    else:
        print(i, end=' ')
    

print(" "*2 +"-"*cols*2)


my_list=[]


for i in range(rows):
    #Creating rows and appending it in list
    inside_list=[]
    for j in range(cols):
        if i==j:
            inside_list.append(1) 
        
        else:
            inside_list.append(0)
    my_list.append(inside_list) #each row is being appended to my_list to create matrix


#Iterating through the inside list of my_list to get output
for i in range(rows):
    print(f"{i}|", end=" ") #row number at the beginning of each row
    for j in range(cols):
        print(my_list[i][j], end=" ")
    print()

