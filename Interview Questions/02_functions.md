### 1. What are first-class functions?
- In Python, functions are first class citizens, which means Functions are treated just like other objects (int, str, list)
- So you can :
    - assign them to varibales
    - pass them as arguments
    - Return them from other functions
    - Store them in data structures
1. **Functions can be assigned to variables**
    ```
        def greet() :
            return "Hello"

        say_hello = greet
        print(say_hello()) # hello
    ```
- Here `greet` is an object
2. **Functions can be passed as arguments**
    ```
        def apply(func, value) :
            return func(value)

        def square(x) :
            return x * x

        print(apply(square, 3)) # 9
    ```
- This is the base of :
    - callbacks
    - Higher order functions
    - Event handlers
3. **Functions can be returned from another functions**
    ```
        def outer():
            def inner():
                return "Hi"
            return inner

        f = outer()
        print(f()) # Hi
    ```
- This enables :
    - Closures
    - Decorators
4. **Functions can be stored in data structures**
    ```
        operations = [str.upper, str.lower]
        print(operations[0]("hello")) # HELLO
    ```

- First-class functions allow powerful features like :
    - Decorators
    - Closures
    - map, filter, reduce
    - functional programming style
    - clean and reusable code

### 2. Explain closure with an example?
- A closure is a function that remembers and accesses variables from its enclosing scope even after the outer function has finished execution.
- Decorators internally uses Closures.
    ```
        def outer_function(message):
            # This variable is in the outer function's scope
            greeting = message

            def inner_function(name):
                # inner_function has access to 'greeting' from outer scope
                return f"{greeting}, {name}!"

            return inner_function

        # Create closures with different messages
        say_hello = outer_function("Hello")
        say_goodbye = outer_function("Goodbye")

        print(say_hello("Alice"))    # Output: Hello, Alice!
        print(say_goodbye("Bob"))    # Output: Goodbye, Bob!
    ```

### 3. How do decorators work internally?
A decorator is a function that takes another function, wraps it inside another function (closure) to extend or modify its behavior, and returns the wrapper. The @ syntax is just shorthand for func = decorator(func).
- When multiple decorators are applied, Python applies them bottom-up (closest to function first), but execution happens top-down (outermost wrapper first).
- To create a decorator with arguments, use a three-layer function structure: outer function for arguments, middle function as the actual decorator, and inner wrapper. Use functools.wraps to preserve the original function’s metadata.

### 4. *args vs **kwargs
- `*args` :
    - Stands for “arbitrary arguments”
    - Collects extra positional arguments into a tuple
    - You can pass any number of positional arguments
    - Inside function → args is a tuple
    ```
        def add(*args) :
            print(args)
            return sum(args)

        print(add(1,2,3,4,5)) # 15
    ```
- `**kwargs`
    - Stands for “keyword arguments”
    - Collects extra named arguments into a dictionary
    - You can pass any number of keyword arguments
    - Inside function → kwargs is a dict
    ```
        def info(**kwargs):
            print(kwargs)

        info(name="Mounika", age=30)
    ```
- Order matters: *args must come before **kwargs in function definition
    ```
        def combined(*args, **kwargs):
            print("args:", args) # args : (1,2,3)
            print("kwargs:", kwargs) # kwargs : {'name': 'Mounika', 'age': 30}

        combined(1, 2, 3, name="Mounika", age=30)
    ```
- `*args` collects extra positional arguments into a tuple, while `**kwargs` collects extra keyword arguments into a dictionary. A function can accept both, modify or add arguments, and forward them to another function using argument unpacking.

### 5. What are function annotations in Python? How do they differ from docstrings, and what practical uses have you found for them in production code?
Function annotations are structured metadata attached to function parameters and return values. Unlike docstrings, they are machine-readable and commonly used for static type checking, IDE support, and framework-level validation, though Python itself does not enforce them at runtime.

### 6. What are Lambda functions?
- A lambda function in Python is a small, anonymous (unnamed) function defined using the lambda keyword.
    - It can take any number of arguments but can only contain a single expression.
    - The result of that expression is automatically returned.
    - Often used for short, throwaway functions where using def would be unnecessary.
- Syntax : `lambda arguments : expression`
    ```
        add = lambda a,b : a + b
        print(add(2,5))   # 7
    ```
- Most commonly used with :
    - map
    - filter
    - max, min
    - sorted
    - event callbacks

### 7. What is List Comprehension ?
List comprehension is a concise and Pythonic way to create lists using expression-based iteration. It improves readability and performance compared to traditional loops, but should be avoided when the logic becomes too complex.

### 8. What does the nonlocal keyword do in Python?
- The nonlocal keyword in Python is used inside nested functions to indicate that a variable refers to the nearest enclosing scope (not global, not local).
- Normally, when you assign to a variable inside a function, Python treats it as local to that function. nonlocal allows you to modify a variable from an enclosing (outer) function’s scope instead.
    ```
    def outer():
        x = 10
        def inner():
            nonlocal x
            x += 5
            print("Inner:", x) # 15
        inner()
        print("Outer:", x) # 15
​
    outer()
    ```
- Without nonlocal, you'd get an error when trying to assign x inside inner()

### 9. How are lambda functions used with map(), filter(), and reduce()? Give examples.
- Lambda functions are frequently used in combination with Python’s built-in functional programming tools: map, filter, and reduce.
- **map(function, iterable)**: Applies a function to every item in an iterable.
    ```
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x**2, nums)) # Output: [1, 4, 9, 16]
    print(squares)
    ```
- **filter(function, iterable)**: Filters items for which the function returns True.
    ```
    nums=[1,2,3,4,5]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    # Output: [2, 4]
    print(evens)
    ```
- **reduce(function, iterable)**: Applies a rolling computation (from functools).
    ```
    from functools import reduce
    nums={2,4,6,2,8,5}
    total = reduce(lambda x, y: x + y, nums)
    # Output: 25
    print(total)
    ```
- These tools combined with lambda allow you to write highly expressive one-liners.

### 10.  How can lambda functions be used with sorted()? Explain with example.
- The sorted() function has a key parameter, which specifies a function to extract the value used for comparison. A lambda function is often passed here (as key parameter) to provide an inline, one-time sorting rule without defining a separate function.
- Example 1: Sort by length
    ```
    words = ["apple", "bat", "banana"]
    sorted_words = sorted(words, key=lambda x: len(x))
    # Output: ['bat', 'apple', 'banana']
    print(sorted_words)
    ```
- Example 2: Sort list of tuples by second element
    ```
    pairs = [(1, 3), (2, 1), (4, 2)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    # Output: [(2, 1), (4, 2), (1, 3)]
    print(sorted_pairs)
    ```
- Using lambda with sorted() is useful for customized sorting, often without needing a named function.

### 11. Can lambda functions return multiple values? Explain with an example.
- Lambda functions in Python are limited to a single expression, but that expression can return multiple values—typically as a tuple or a list.
- Example:
    ```
        f = lambda x, y: (x + y, x * y)
        result = f(3, 4)
        print(result)  # Output: (7, 12)
    ```
- Although lambdas don’t use the return keyword, the result of the expression is returned implicitly. You can use lambdas to quickly return combinations of values, such as sum and product, min and max, etc.
- Note: if the logic becomes complex or requires multiple steps, a regular def function is more appropriate.

### 12. How does Python handle variable scope and closures?
- Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve variables in different scopes.
    - `Local (L)`: Variables defined inside the current function.
    - `Enclosing (E)`: Variables in the enclosing functions (for nested functions).
    - `Global (G)`: Variables declared at the top level of a module or using global.
    - `Built-in (B)`: Names predefined in Python (like len, sum).
- A closure occurs when a nested function captures variables from its enclosing scope and remembers their values, even after the outer function has finished execution. Closures are useful for encapsulation, decorators, and callbacks.
- Example:
    ```
        def outer(x):
            def inner(y):
                return x + y
            return inner
        ​
        closure_func = outer(10)
        print(closure_func(5))  # Output: 15
    ```
- Here, inner remembers the value of x from outer even after outer has finished. Python stores these variables in the function’s `__closure__` attribute.

