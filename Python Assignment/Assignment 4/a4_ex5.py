
#Insertion sort implementation
def sort(elements: list, ascending: bool):
    
    for i in range(1, len(elements)):
        j=i
        while elements[j-1] > elements[j] and j>0:#to check if the left neighbour is greater than the current element and the index cannot be less than 0
            elements[j-1], elements[j]= elements[j], elements[j-1] #Swapping
            j-=1

    return elements if ascending==True else elements[::-1]


# print(sort([1,56,23,9,0,4], True))
print(sort([1,56,23,9,0,4], False))