

the_list=[]

while True:
    user_input=input("Enter element or 'x' when done: ")

    if user_input == 'x':
        break
    
    the_list.append(user_input)


unique_sorted_list=sorted(set(the_list))



print("all:", the_list)
print("unique (sorted):", unique_sorted_list)
    
    

