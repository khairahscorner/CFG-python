import math


def some_function(name, job='developer'):
    print(name, 'is a', job)

some_function('Airah', 'manager')

for number in range(9):
    print('~' * number)

price = input("Enter burger price: ")
is_less = float(price) <= 10.00

print("Burger is within budget: {}".format(is_less))

# question 1
# def check_is_raining():
#     response = input("Is it raining?: ")
#     while response != 'y' and response != 'n':
#         response = input("Invalid. Is it raining?: ")
#     if response == 'y':
#         print("Take an umbrella")
#     else:
#         print("You don't need an umbrella")
#
# check_is_raining()

# question 2
my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if int(my_money) < boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')


# question 3

year = input("enter year: ")
century = math.floor(int(year)/100)

# is_century = century == 19 ? "Twentieth century" : "Nineteenth"