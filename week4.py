# carrots = input('How many carrots do you have? ')
# rabbits = 6
# if rabbits > int(carrots):
#     print('There are not enough carrots')
# elif rabbits < int(carrots):
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')


names = ["Zoey", "Will", "Abby", "Catherine"]

print(names[1])

clothes = ["shorts", "shoes", "t-shirt"]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"

print(clothes)

scores = [12, 34, 12, 35, 67, -13]

print("number of scores: {}".format(len(scores)))

print("Highest score: {}".format(sorted(scores)[len(scores) - 1]))
print("Highest score: {}".format(max(scores)))

print("Lowest score: {}".format(sorted(scores)[0]))
print("Lowest score: {}".format(min(scores)))

print(list(reversed(sorted(scores))))


shopping_list = ["baking soda", "salt", "sugar", "eggs"]
if "bread" in shopping_list:
    shopping_list.append("butter")

print(shopping_list)

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place["location"])
print(place["location"]["latitude"])

