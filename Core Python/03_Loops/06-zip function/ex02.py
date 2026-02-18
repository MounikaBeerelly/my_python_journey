#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"Zip\" function in python")
print("--------------------OoO-------------------")

itemsinBasket = ["Scissors", "Paper Packs", "Glue Sticks", "Erasers", "Staple Pins"]
itemsQuantity = [10,25, 15, 20, 5]

#finalBasket = zip(itemsinBasket, itemsQuantity) #Here the address to the location of the zipped object is returned
#print("\nThe final basket is:", list(finalBasket), end="\n")

print("The final basket with Items and Quantity..", end="\n")

print(list(zip(itemsinBasket,itemsQuantity)), end="\n")

for basketItem, itemQuantity in zip(itemsinBasket,itemsQuantity):
    print(basketItem,itemQuantity, end="\n")