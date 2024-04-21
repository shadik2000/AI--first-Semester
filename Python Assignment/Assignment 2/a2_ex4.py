#Asking user to enter number of hyphens they want

rows= int(input("Enter number of lines: "))

if rows>3:
    print(rows*"-")
    for i in range(1,rows-1): 
        print("|"+(rows-2)*" "+"|")      
  
    print(rows*"-")
        

else:
    print("Invalid number of lines")
    
