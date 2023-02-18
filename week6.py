# import requests
from pprint import pprint
#
# pokemon_number = input("What is the Pokemon's ID? ")
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# response = requests.get(url)
# print(response.status_code)
# pokemon = response.json()
# pprint(pokemon)


import requests
url = 'https://pokeapi.co/api/v2/item/28/'
response = requests.get(url)
data = response.json()
# pprint(data["names"])

for name in data["names"]:
    print(name["language"]["name"])
