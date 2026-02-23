#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a Two dimension array using arange function in integration with reshape() function...",end="\n")

myArray01 = np.arange(1,13)
print(f"\nPrinting the elements from the array01...",end="\n")
print(myArray01)

myArray02 = np.arange(1,13).reshape(3,4)
print(f"\nPrinting the elements from the array02...",end="\n")
print(myArray02)
