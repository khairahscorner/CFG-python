import math

print("Hello")
print("Airah is taking a beginner course")
print("qwee" + str(3))

no_of_cats = 10
no_of_cans_per_cat = 3

qwe = "{} Total number of cans: ".format(no_of_cats * no_of_cans_per_cat)
print(10 * "3")

# question 1
chairs = 15
nails = 4

total_nails = chairs * nails
message = "I need to buy {} nails".format(total_nails)
print("{}. Breakdown {} chairs + {} nails per chair".format(message, chairs, nails, total_nails))


# question 2
my_name = "Penelope"
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)


eggs_per_box = 6
eggs_per_omelette = 4

no_of_egg_boxes = input("How many boxes of eggs are in the fridge?: ")
no_of_omelettes = (int(no_of_egg_boxes) * eggs_per_box)/eggs_per_omelette

print("You can make {} omelettes with {} boxes of eggs".format(int(no_of_omelettes), no_of_egg_boxes))




