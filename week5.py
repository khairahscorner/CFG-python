# starter
dictionaries = [
    {"species": "herbivore"},
    {"species": "carnivore"}
]
for diction in dictionaries:
    print(diction["species"])


new_txt = input("enter new text")

with open("text.txt", "r") as txt_file:
    read_list = txt_file.read()
    print(read_list)

    read_list += new_txt + "\n"

with open("text.txt", "w+") as txt_file:
    txt_file.write(read_list)

with open("text.txt", "r") as txt_file:
    read_list = txt_file.read()
    print(read_list)


import csv
# FOR CSV
field = ["name", "age"]
data = [
    {"name": "Airah", "age": 23},
    {"name": "Aisha", "age": 26},
    {"name": "Tawakalt", "age": 22}
]

with open("species.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)
    # or use this
    # for diction in data:
    #     spreadsheet.writerow(diction)

with open("species.csv", "r") as csv_file:
    spreadsheet = csv.DictReader(csv_file, fieldnames=field)

    # csv has key(header) and value(the value for each row), hence using the code below
    for row in spreadsheet:
        print(row)
        # print("Name: " + row["name"])

