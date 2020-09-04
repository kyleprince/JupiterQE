import random
import string
import datetime
import array

# KeyEntry Function
def keyEntry():
    # Open file and set datetime
    file = open('./db.csv', 'a')
    d = datetime.datetime.now()

    # Create variable buckets
    letters = string.ascii_lowercase
    caps = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%&?+"
    allchar = letters + caps + digits + special

    print("Ingredient: ")
    ingr = input()
    print("Profile: ")
    prof = input()
    print("Sec Profile: ")
    secprof = input()
    print("Use: ")
    use = input()
    print("Sec Use: ")
    secuse = input()

    
    file.write(ingr + "," + prof + "," + secprof + "," + use + "," + secuse + "\n")
    file.close()

# Main
keyEntry()
