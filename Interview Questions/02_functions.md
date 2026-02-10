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