
#Asking the duration of subscription from user
number_of_months=int(input("Please enter the duration of your subscription (in months):"))

#Checking the duration and calculating actual price needed to be paid for the subscription

if(number_of_months<=0):
    print("Invalid subscription duration")

elif(number_of_months<6):
    subscription_price=number_of_months*6.5
    print("The price per month is 6.50")
    print(f"The full price for {number_of_months} months is {subscription_price:.2f}")
    
elif(number_of_months>=6 and number_of_months<12):
    subscription_price=number_of_months*5.90
    print("The price per month is 5.90")
    print(f"The full price for {number_of_months} months is {subscription_price:.2f}")
    
else:
    postal_code = int(input("Please enter your postal code:"))

    if(postal_code<1000 or postal_code>9999):
        print("Invalid postal code")

    else:
        p1=postal_code%1000
        p2=p1//10
        monthly_price=4 + p2*0.01

        subscription_price=monthly_price*number_of_months
        
        print(f"The price per month is {monthly_price}")
        print(f"The full price for {number_of_months} months is {subscription_price:.2f}")
    


