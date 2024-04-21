
previous_number = -1
#The while loop will run until the entered string is "x" or the ones place of previous number and current number is different
while True:
    
    current_string=input("Enter number or 'x' : ")
    
    if current_string == "x":
        if previous_number==-1:
            print("Empty sequence")
        
        else:
             print("All numbers had the same digit in the ones place")
        
        break


    elif current_string.isdigit():        
        current_number=int(current_string)
        if previous_number==-1 or (previous_number%10 == current_number % 10):
            previous_number = current_number
            
        else:
            print(f"{previous_number} and {current_number} differ in the ones place")
            break            
    
    
    

    

    