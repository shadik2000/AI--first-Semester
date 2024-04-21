start=int(input("Start: "))
stop=int(input("Stop: "))
step=int(input("Step: "))
count_even=0
sum_odd=0
iteration_number=0


for i in range(start, stop, step):

    if i%2==0:
        count_even+=1

    elif i%2!=0:
        sum_odd+=i


    if iteration_number <5:
        print(f"Number in iteration {iteration_number} = {i}")

    iteration_number+=1

print(f"Even number count = {count_even}")
print(f"Sum of odd numbers = {sum_odd}")


    