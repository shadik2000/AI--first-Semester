

def split_list(lst:list, num_sublists: int) -> list:
    if num_sublists==0:
        print(lst)
    
    else:
        min_elements =len(lst)//num_sublists #the minimum number of elements sublists can have
        max_elements =len(lst)//num_sublists+1 ##the maximum number of elements sublists can have is 1 more than the minimum
    
        num_of_maximum_sized_list=len(lst) % num_sublists #from the remainder, 1 is equally distributed till the remainder is used to create maximum sized sublist

    sublists=[]
    start=0


    
    for i in range(num_sublists):
        num_items=0
        
        if i<num_of_maximum_sized_list:
            num_items=max_elements #maximum number of items in sublist
        
        else:
            num_items=min_elements #minimum number of items in sublist
        
        individual_sublist=lst[start:start+num_items] #Slice list to create sublist
        
        sublists.append(individual_sublist)
        
        start+=num_items
    
    print(sublists)



# split_list([0,1,2,3,4], 2)
# split_list([0,1,2,3], 1) 
# split_list([0,1,2,3,4,5,6,7], 3)