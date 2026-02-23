#! python3

import os
os.system("cls")
import numpy as np

temparatureData = np.array([22.5, 24.0, 23.8, 25.3, 26.1, 27.0, 23.5])

print(f"\nThe recorded temparatures in this week: {temparatureData}", end="\n")

inTempIndex = int(input("\nPlease enter the week day to extract the temparature : "))

if inTempIndex >= 1 and inTempIndex <= 7:
    print(f"\nThe requested temparature for day {inTempIndex} of this week is : {temparatureData[inTempIndex]}", end="\n")
else:
    print(f"\nHey! The given week day {inTempIndex} is out of the boundary", end="\n")