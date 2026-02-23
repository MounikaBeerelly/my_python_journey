#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a two dimension array of 3*5 order using list...",end="\n")

myArray1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray1)

myArray2 = np.array([[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray2)

print(f"\nCombining two array into a final array...",end="\n")
finalArray = np.concatenate((myArray1,myArray2))
print(finalArray)


"""
When arrays are concatenated, Two different arrays of "Different row order, having same column order" can be concatenated
"""