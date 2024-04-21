#a small order form for a store that sells PC parts 

print(63*"=")
print("PC Parts Store- Order")
print(63*"=")

cable=int(input("Number of cables: "))
monitor=int(input("Number of monitors: "))
keyboard=int(input("Number of keyboards: "))

cost_of_cables=float("{:.2f}".format(9.90*cable))
cost_of_monitors=float("{:.2f}".format(249.99*monitor))
cost_of_keyboards=float("{:.2f}".format(27.50*keyboard))

total_cost=cost_of_cables+ cost_of_monitors+ cost_of_keyboards
# total_cost1="{:.2f}".format(total_cost)

print(f" {cable} cables (9.90 EUR each) = {cost_of_cables} EUR")
print(f" {monitor} monitors (249.99 EUR each) = {cost_of_monitors} EUR")
print(f" {keyboard} keyboards (27.50 EUR each) = {cost_of_keyboards} EUR")

print(63*"-")

print("Total:", total_cost, "EUR")
