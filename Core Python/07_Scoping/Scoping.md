### What is Scoping in Python ?
1. Any Identifier declared in python application can only be accessed in the area to which it is defined, this concept is called as Scope.
2. Once the scope of the identifier is lost then that identifier is no more available in the operational memory of the application, hence it is lost from the applications memory.
3. Within the same scope two identifiers cannot have the same name.
4. In Python the scope of the identifier is managed by a concept of rule called as `LEGB` rule.
5. All the python identifiers resolve the names in operational process in run time by using the LEGB rule, where LEGB stands for
    - `L` : Local, Functional scope
    - `E` : Enclosing, Non-local scope
    - `G` : Global, Module scope
    - `B` : Built-in, Programming language level
6. When a Python program is in execution the order of search for finalizing the scope of the identifier is executed in the order of `local -> Enclosing -> Global -> Built-in`

#### Note:
1. All the operations that are as part of the functions definition are considered to be in local scope of the function.
2. Local scope is visible only when the function is called.

### Concepts to be remembered when operating with the `Enclosing Scope` :
1. `Enclosing Scope` arises only when we are having `Nested Functions`.
2. Inner function accessing the outer function scope is `Enclosing Scope`
```
def outerFunction():
    "The local scope of the outer function begins here"

        1. Global scope of the program level
        2. Local scope of the outer function level
        3. Built-in scope of the programming language level

    def innerFunction() :
        "The local scope of the inner function begins here"

        1. Local scope of the inner function (first priority)
        2. Enclosing Scope of the outer functions local scope
        3. Global scope of the program level
        4. Built-in scope of the programming language level

        return
        "The local scope of the inner function ends here"

    return
    "The local scope of the outer function ends here"
```

### What is meant by Closure ?
1. A `Closure` is the "Combination of a function bundled together with all its references to its surrounding spaces".
2. A `Closure` is a technique for implementing "lexically scoped name binding with respect to any programming language with the concept of `First class functions`".
3. Closures are possible in Python when
    1. We have a nested function: Outer function containing the definition of the inner function
    2. The nested function refers to a variable of the outer function
    3. The enclosing function "Returns the enclosed function".

### What are Partial Functions:
1. A Partial Function in general is a `Mathematical OR Computational` concept, where a function is defined for some but not all possible inputs of its domain.
    - **Point to Note** : A Total function is a function that is defined for every input in its domain.
2. A Partial function can be considered as a function that
    - Is only defined for a subset of its input space i.e. its domain
    - May not produce an output for every possible input
3. As per Computer Science, Partial functions are used when a function can handle only certain inputs OR when the behavior of the function is undefined for certain conditions.
4. Partial Functions model situations where "certain operations OR computations aren't valid for all possible inputs".


### What are Decorators in Python :
1. A `Decorator` is also a function in Python
2. A `Decorator` is a special kind of function, that takes **Another function as its argument** and **Returns yet another function**.
3. A `Decorator` is extremely necessary when we want to **extend the existing function without any modification to the original functions source code**.

#### Basic Syntax :
```
    def decoratorFunction() :
        Operational code

    @decoratorFunction
    def operationalFunction() :
        operational code

    operationalFunction()
```


### Higher Order Function:
- A function which accepts another function as parameter is called `Higher Order Function`.