#!python3

import os
os.system("cls")

class EmptyClass :
    pass

emptyClassObject01 = EmptyClass() # Creating Instance of the class : object
print("\n\nThe reference address of the object is : ", emptyClassObject01, end="\n")

emptyClassObject02 = EmptyClass() # Creating Instance of the class : object
print("\n\nThe reference address of the object is : ", emptyClassObject02, end="\n")


"""
Output:
======

The reference address of the object is :  <__main__.EmptyClass object at 0x00000276446A1FD0>


The reference address of the object is :  <__main__.EmptyClass object at 0x00000276446A1FA0>

"""