### Understanding NameError in Python :
1. NameError is raised when a local OR Global Name is not found in the "Execution Module"
2. The name can be any identifier in Python currently running application like
    1. Variable Name
    2. Function Name
    3. Module Name
    4. Package Name
3. We can even raise the NameError explicitly, when needed by using
    - **Syntax** :
        ```
        raise NameError("Required Message")
        ```
### Understanding the `traceback` module in Python :
1. The `Traceback` module in Python is a "Built-in" module.
2. The `traceback` module provides functions for handling "Stack Traces" of the Python programs for
    1. Extarcting
    2. Formatting
    3. Printing