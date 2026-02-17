### 1. How is Exceptional handling done in Python?
- Exception handling in Python is done using try, except, else, and finally blocks. It allows a program to catch and handle runtime errors gracefully without crashing.
- `try` : Try block is used to check some code for errors i.e, the code inside try block will execute there is no errors in the program
- `except` : Executes when an error occurs in the try block.
- `finally` : Executes after the try and except blocks, regardless of whether an error occurred. It’s used for cleanup tasks.
- **Example:** Trying to divide a number by zero will cause an exception.
```
    n = 10
    try:
        res = n / 0  # This will raise a ZeroDivisionError

    except ZeroDivisionError:
        print("Can't be divided by zero!")

Output
Can't be divided by zero!
```
- Explanation: In this example, dividing number by 0 raises a ZeroDivisionError. The try block contains the code that might cause an exception and the except block handles the exception, printing an error message instead of stopping the program.

### 2. What are Decorators?
- Decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code. A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
- Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

### 3. How do you debug a Python program?
- `Using pdb (Python Debugger):` pdb is a built-in module that allows you to set breakpoints and step through the code line by line. You can start the debugger by adding import pdb; pdb.set_trace() in your code where you want to begin debugging.
    ```
        import pdb
        x = 5
        pdb.set_trace()  # Debugger starts here
        print(x)
    ```
- `Using logging Module:` For more advanced debugging, the logging module provides a flexible way to log messages with different severity levels (INFO, DEBUG, WARNING, ERROR, CRITICAL).
- For logical bugs, I write targeted unit tests to isolate the issue.

### 4. What are Iterators in Python?
- An iterator is an object that allows you to traverse (loop through) elements one at a time.
- It implements two special methods:
    - `__iter__()` : returns the iterator object
    - `__next__()` : returns the next value
- When there are no more elements, it raises: `StopIteration`
    ```
        numbers = [1, 2, 3]

        iterator = iter(numbers)   # Get iterator object

        print(next(iterator))  # 1
        print(next(iterator))  # 2
        print(next(iterator))  # 3
        print(next(iterator))  # Raises StopIteration
    ```

### 5. What are Generators in Python?
- A generator in Python is a special type of iterator created using the yield keyword. It produces values one at a time and maintains its state between calls, making it memory efficient. Generators are useful when working with large datasets or streaming data because they avoid loading everything into memory at once.
- Normal Function
    ```
        def square(n):
            return [i*i for i in range(n)]
    ```
    - Creates full list in memory
- Generator Function
    ```
        def square(n):
            for i in range(n):
                yield i*i
    ```
    - Generates one value at a time
    - Much more memory efficient