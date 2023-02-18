import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

path = './recipes.csv'
check_file = os.path.isfile(path)


# saved API details to .env file. can be added directly here and used

def get_recipes(url):
    response = requests.get(url)
    process_results(response.status_code, response.json())


def process_results(status, response):
    # pprint(response)
    if status == 200:
        print("There are {} recipes available.".format(response["count"]))
        if response["count"] > 0:
            print("Now showing recipes {} to {}.\n".format(response["from"], response["to"]))
            counter = response["from"]

            if not check_file:
                write_recipe_header()

            new_list = order_by_prep_time(response["hits"])
            for recipe in new_list:
                print("{}) {}  - Prep. Time: {}".format(counter, recipe["recipe"]["label"],
                                                        recipe["recipe"]["totalTime"]))
                index = 0
                print("Ingredients you need:")
                for ing in recipe["recipe"]["ingredientLines"]:
                    if index == len(recipe["recipe"]["ingredientLines"]) - 1:
                        print("- {}.\n".format(ing))
                    else:
                        # print("{}, ".format(ing), end='')
                        print("- {}, ".format(ing))
                        index += 1
                counter += 1

                save_recipes_to_file(recipe["recipe"])

            if response["_links"]:
                next_recipes = input("Would you like to check the next results? Enter 'y' for Yes, 'n' to check another"
                                     " ingredient, or anything else to exit: ")
                if next_recipes.lower() == 'y':
                    get_recipes(response["_links"]["next"]["href"])
                elif next_recipes.lower() == 'n':
                    print("\n\n")
                    start_program()
            else:
                another_recipe = input(
                    "Would you like to check for another recipe? Enter y for Yes or anything else to exit: ")
                if another_recipe.lower() == 'y':
                    print("\n\n")
                    start_program()

        else:
            another_recipe = input(
                "Would you like to check for another recipe? Enter y for Yes or anything else to exit: ")
            if another_recipe.lower() == 'y':
                print("\n\n")
                start_program()

        # SAVE RESULTS?

    else:
        print("An error occurred. Try again later")


def order_by_prep_time(list_to_sort):
    return sorted(list_to_sort, key=lambda x: x["recipe"]['totalTime'])
    # return sorted(list_to_sort, key=lambda x: x["recipe"]['totalTime'], reverse=True) #Descending order


def write_recipe_header():
    fields = ["Recipe Name", "Prep. Time", "Ingredients"]
    with open("recipes.csv", "w+") as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=fields)
        spreadsheet.writeheader()


def save_recipes_to_file(recipe):
    # For adding to file
    fields = ["Recipe Name", "Prep. Time", "Ingredients"]
    all_ingredients = "["
    index = 0

    for ing in recipe["ingredients"]:
        if index == len(recipe["ingredients"]) - 1:
            all_ingredients += "{}.]".format(ing["food"])
        else:
            all_ingredients += "{}, ".format(ing["food"])
            index += 1

    # append to file
    with open("recipes.csv", "a") as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=fields)
        spreadsheet.writerow(
            {"Recipe Name": recipe["label"], "Prep. Time": recipe["totalTime"], "Ingredients": all_ingredients})


def start_program():
    search = input("What recipe are you looking for (ingredient or food name)? ")

    url = "https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}".format(search,
                                                                                               os.environ["api_id"],
                                                                                               os.environ["api_key"])
    # url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(search, api_id, api_key) #old API
    get_recipes(url)


start_program()
