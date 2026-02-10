# What are Variable Argument Functions in Python ?

## Non-Keyword argument ( *args )
1. *args in functions signature instructs the interpreter that this function will get the intelligence about the number of parameters OR values only at run time (Execution of the function)
2. Because of the `Unpacking operator : *`, the process at run-time can become iterable and the function can take the values by iterating over the "args" object.

## Keyword argument ( **kwargs )
1. Keyword Arguments are arguments that are passed to a function with a `key-value` pair.
2. Keyword Arguments are represented as `**kwargs`.
    - The **kwargs syntax allows the function to accept an arbitary number or keyword arguments.
    - **kwargs syntax collects the given arguments into a Python collection called as `Dictionary`.
        - Keys are treated as `Argument Names`
        - Values are the corresponding arguments that represent `actual values`.

#### Basic Syntax:
    ```
    def functionName(**kwargs) :
        # function body goes here
    ```