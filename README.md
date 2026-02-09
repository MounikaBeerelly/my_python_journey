- `%d`
    - type format indicators, It represents the value will be an integer.
    - These type format indicators in print() function will act as placeholder, To reference the actual data in that position that will be printed at run time.

- `print(f"\nCreating a single dimension array...", end="\n")`
    - The f before the string — means it’s an f-string (formatted string literal) in Python.
    - It allows you to easily insert variables or expressions

- `string interpolation`
    - ```
      myName = 'John'
      print("My name is:",myName)
      print("My name is: %s"%(myName))
      print(f"My name is: {myName}")
      ```
### Understanding Multi-Conditional `if` implementation

1. Multiple conditions can be handled in python using Logical "and" and "or" operators.
    1. `and` operator finally returns true only when all the conditions are evaluated to `True`.
    2. `or` operator finally returns truw only when any one of the conditions is evaluated to `True`.

### Understanding the concept of `nested if`
1. Nested if is a scenario where, the true state of one "if" is immediately followed by another "if"
    - **Syntax**
        ```
        if<Condition01>:
            if<Condition02>:
                if<Condition03>:
                    operations of the TRUE state of condition 03
                else:
                    Operations of the FALSE state of condition 03
            else:
                Operations of the FALSE state of condition 02
        else:
            Operations of the FALSE state of condition 01
        ```

### Understanding the concept of "elif" in python branching

1. The `elf` is a keyword in python
2. `elif` keyword is a short form of "else if", used in control flow statements.
3. For every false condition of the `if` branch, when we have an alternate condition to be checked under the "False" state of the "if" we need `elif`.

### What is meant by iteration in programming?
- `Iteration` in computer programming is a concept of Executing the same block of code OR instruction(s) over and over, for multiple time, without replacing the insctructional code in the source multiple times.
- The program structure that implements the concept of iteration is called as `loop`.
- Every iteration should have five components to make the iteration to the situation.
    1. Initialization
        - defines the starting point of the looping process.
    2. Condition
        - defines the state under which the iteration can actually begin OR continue OR terminate.
    3. Action
        - Is any operational statement OR instruction that are expected to be the goal of the logical implementation as part of the code OR application.
    4. Updation
        - is any kind of operational instruction that modifies the initial state of the iteration of the loop to enter into the next level of the iterative process OR looping process. To make actions look new to the next level of the real time environment.
    5. Termination
        - Is a state that makes the iterative process to quit and keeps the program to get into the next level of the instruction in the program surface.

**Types of Iterations:**
1. Definite Iteration (Finite iteration)
2. In-definite Iteration(In-finite iteration)
**Types of iterations by Imeplementation**
1. Pre-tested loop
2. post-tested loop
**Types of loops:**
1. `while loop`
    - While loop falls under the "pre-tested" loop construct.
    - while loop executes a block of statements repeatedly, only when the condition is "True".
    - **Syntax**
        - ```
           while conditionalExpression:
              loop execution statement 01
              loop execution statement 02
              loop execution statement 03
              loop execution statement 04
          ```
2. `for loop`
    - **for** loop in python is very dynamic with its state of execution.
    - **for** loop generally operates on the logic of range evaluation, where the range is "iterable" by indexing.
    - Every "for" loop has at-least one indexing variable, which is auto declared and n=managed as the loop is advancing.
    - "for" loop contains "in" keyword which actually identifies the object on which the iteration has to be implemented.
    - **Syntax**
        -   ```
                for<indexing> in <range>:
                    statements
            ```
            - By default if not mentioned range, range intializes from 0, and continues to the nth value

### Understanding "zip()" function in for loop:
- It is built-in function in Python namespace.
- zip() function accepts `iterable objects` OR `container objects` as an argument and returns A `singe iterator object`.
- The returned `single iterator object` will be having mapped values from all the containers that are supplied.
- "zip()" built-in function is mostly used to `map smallar index of multiple containers` to be handled as a `single entity`.
    - Basic syntax:
        - `zip("IteratorObjects)`

### Understanding "enumerate" function in for loop:
- "enumerate()" function is built-in function that can enumerate the data values that are extracted from the collection.
- "enumerate" function adds a counter to an iterable object and returns the iterablr object as an "enumerating object" allocating one counter value for each element that is extracted.
- Syntax:
    - `enumerate(iterableObject, start=0)`

### Understanding Nested loops concept:

1. A loop in general is a continuous operations that is executed until a condition is satisfied.
2. A loop is control flow statement that allows "Instructions" to be executed repeatedly as long as a given condition is "true".
3. When nested loops are implemented, one loop is integrated with another loop associating to the "control state" validated at each level of the individual loop.

**Applications of Nested Loop**:
1. Matrix OR Grid traversals
2. Menu Driven programs
3. Handling Input Validations
4. Counting and Accumulating
5. Table Management
6. 2D and 3D implementations


### Understanding functions design approches

1. There are four different approaches when designing functions
    1. Function not accepting parameters and function not returning any value
    2. Function accepting parameters and functions not returning anu value
    3. Function not accepting parameters and function returns a value
    4. Function accepting parameters and function returning a value

### Note:
1. As in Python everything is an object, Python does not has the concept of
    1. Call-By-Value
    2. Call-By-Reference
2. When a function is called, Python operates on the principle of `Call-By-Object`
    1. Every parameter OR an argument given to python function at the time of calling is considered as an object.
        - Hence every parameter OR an argument of the Pythons function has its own `Allocated Object ID`
3. Any parameters calling in the function is `Actual parameters`
4. `Formal Parameters` - part of function definition

- When a function is designed, the developer can plan the arguments in two ways
    1. Mandatory Arguments
    2. Optional OR default arguments

### Note:
1. When we call any function by just passing the values as actual parameters, the given actual parameter values in actual environment will be copied into the "Formal Parameters" of the function definition exactly as per the declared position of the "Formal Parameters", this kind of parameter substitution by exact position is called as `Positional Notation`.
- **Basic Illustration :**
    ```
    def addValues(inOperand01, inOperand02) :
                       ^             ^
                       |             |  Positional notation
            addValues(operand01, operand02)
    ```
- When positional notation is used in function call, all the supplied "Actual Parameters" should follow the exact order of declaration defined in the "Functions Definition".
    - Any time the order of the "Actual Parameters" in the "Fucntion call" is mis-matching to the declared order of the "types" of the "Formal Parameters" either
        - Logically the operational state of the function will be wrong OR
        - The function at run-time can generate an error due to "Type Mis-Match"
