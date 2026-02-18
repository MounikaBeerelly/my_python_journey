### 1. What is Object-Oriented Programming (OOP) in Python?
- Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code using classes and objects, where objects are instances of classes that encapsulate both data (attributes) and behavior (methods).
- OOP in Python follows the core principles of object-oriented design — encapsulation, abstraction, inheritance, and polymorphism.
- **Key Characteristics of OOP in Python** :
1. Dynamic Typing :
    - Python does not require explicit type declarations for attributes or method parameters. Types are determined at runtime, making OOP more flexible compared to statically typed languages.
2. Everything is an object :
    - In Python:
        - Integers
        - Strings
        - Functions
        - Classes are all objects.
3. Multiple Inheritance :
    - Python allows a class to inherit from multiple parent classes
4. Duck Typing
    - Python focuses on behavior rather than explicit type hierarchy.
5. Built-in Methods
    - Python provides special methods to integrate objects with built-in operations.
        - __init__ → constructor
        - __str__ → string representation
        - __len__ → length behavior
        - __add__ → operator overloading

### 2. What are the key features of OOP?
The key features of oop are:
- Encapsulation: Bundles data and methods within a class, hiding internal details from outside access.
- Abstraction: Hides complex implementation details and exposes only necessary functionality.
- Inheritance: Allows a new class to inherit properties and methods from an existing class.
- Polymorphism: Enables a single interface to represent different behaviors.

### 3. What is a class and an object in Python?
A class in Python is a blueprint that defines attributes and methods, while an object is an instance of that class containing actual data. Classes define structure and behavior, and objects represent real-world entities created from that structure.

### 4. What is the __init__ method in Python?
- The `__init__` method in Python is a special constructor method that automatically runs when a new object of a class is created.
- It is used to initialize the object’s attributes with default or user-provided values.
- It is similar to constructors in other OOP languages like Java or C++.
- Example:
    ```
        class Person:
            def __init__(self, name):
                self.name = name

        p = Person("Magnus")
        ​
        print(p.name)  # Magnus
    ```

### 5. What is self in Python classes?
`self` is a reference to the current instance of the class. It is used to access attributes and methods of the class. When you define a method inside a class, the first parameter of the method is always self, which allows the method to refer to the object (or instance) on which the method was called.

### 6. What is the difference between instance variables and class variables?
- Instance variables belong to a specific object of a class and are defined inside methods using self (e.g., self.name). Each object gets its own copy, so modifying one instance’s variable does not affect others.
- Class variables, on the other hand, are defined directly inside the class but outside methods. They are shared across all objects of that class, so changing a class variable affects every instance (unless it is overridden at the instance level).
Example:
```
    class Demo:
    class_var = "shared" # class variable

    def __init__(self, val):
        self.instance_var = val # instance variable
```

### 7. What is inheritance in Python?
- Inheritance allows a class to inherit attributes and methods from another class. Inheritance enables the child class to inherit the properties (attributes) and behaviors (methods) of the parent class, and it can also define its own additional attributes and methods or override existing ones.
- Example:
    ```
        # Define the Parent class (base class)
        class Parent:
            pass
        ​
        # Define the Child class that inherits from Parent class
        class Child(Parent):
            pass
    ```

### 8. What is method overloading in Python?
- Method overloading means defining multiple methods with the same name but different parameters in the same class.
- Unlike Java or C++, Python does not allow multiple methods with the same name in the same class.
- If you define multiple methods with the same name, the last one overrides the previous ones.
- Example (Not Working Like Java)
    ```
        class Example:
        def add(self, a, b):
            return a + b

        def add(self, a, b, c):   # This overrides the first one
            return a + b + c
    ```
- Only second add() exists
- **How Python Achieves Method Overloading**
    - Python handles it differently using:
        1. Default arguments
        2. Variable-length arguments (*args)
        3. Keyword arguments (**kwargs)
        4. Type checking inside function