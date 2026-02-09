#!python3 #python version interpreter

import os
os.system("cls")

print("Hello everyone, I started learning Python")

"""
- An EOL error indicates that within the represented line, the string is not properly terminated.
- Semicolon after any python statement not an error, but it is not compulsory.
"""
print("\nWelcome to the world") #\n for adding new line before printing the data.


print("Welcome to the world", end="")

"""
- The developer can customize the "end" parameter in the "print()" function.
- If we don't want the new line immediately after printing the data onto the output console, we can construct "print()" function by defining the "end" parameter assigned with "empty quotes".
- Illustration:
    print("------------", end="")
"""
print("Welcome to the world", end="\n") #when we force the new line character, the print overrides the default for end parameter.

print("My Name is : John Doe\nMy FirstName is : John\nMy LastName is : Doe")

print("My name is:","John","Doe"); #when we are giving multiple objects seperated by comma, it gives space between objects.
