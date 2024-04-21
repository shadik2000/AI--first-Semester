
def clip(*values, min_=0, max_=1) -> list:
    my_list=[]

    for item in values:
        if item<min_:
            my_list.append(min_)
        
        elif item>max_:
            my_list.append(max_)
        
        else:
            my_list.append(item)

    print(my_list)


""" Outputs """

# clip() #[]
# clip(1, 2, 0.1, 0)  #[1, 1, 0.1, 0]
# clip(-1, 0.5) #[0, 0.5]
# clip(-1, 0.5, min_=-2) #[-1, 0.5]
# clip(-1, 0.5, max_=0.3) #[0, 0.3]
# clip(-1, 0.5, min_=2, max_=3) #[2, 2]