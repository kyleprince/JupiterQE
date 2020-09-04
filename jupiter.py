import json
import csv

# Define dictionary
print("Ingredient: ")
#entry1 = input()
print("Profile: ")
#entry2 = input()


with open('db.csv', newline='') as csvfile:
    ing_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in ing_reader:
        print(', '.join(row))


        