#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a Single dimension array using linspace function in integration with reshape() function...",end="\n")

myArray01 = np.linspace(0,1,10)
print(f"\nPrinting the elements from the array01...",end="\n")
print(myArray01)

myArray02 = np.linspace(0,10,5)
print(f"\nPrinting the elements from the array03...",end="\n")
print(myArray02)

myArray03 = np.linspace(0,10,5, endpoint=False)
print(f"\nPrinting the elements from the array03...",end="\n")
print(myArray03)

myArray04,stepValue = np.linspace(0,10,5, retstep=True)
print(f"\nPrinting the elements from the array04...",end="\n")
print(myArray04)
print(f"\nThe step value fixed is: {stepValue}",end="\n")

myArray05 = np.linspace(0,10,5, dtype=int)
print(f"\nPrinting the elements from the array05...",end="\n")
print(myArray05)

"""

Generated Output:
----------------
Printing the elements from the array01...
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]

"""