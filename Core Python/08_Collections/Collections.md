### What are Python Lists :
1. Python `List` is a sequence datatype structure, with self-indexing feature, used to store `Multiple Continuous Elements` in a single variable.
2. List is a Built-in datatype in Python which is used to store collections of data.
    1. List Sequence type is Managed in python using `list type class`.
    2. List sequence type will have its own constructor by name `list()`.
3. List object instance is created in Python in two ways :
    1. Using the notation of square brackets `[]`
    2. Using the `list()` constructor of the "list" class.
4. Python list can accomodate Heterogeneous OR Homogeneous data by requirement, hence a list can contain a mixed collection of
    1. Integers
    2. Floats
    3. Strings
    4. Objects
    5. Nested List
    7. Any other sequence type
5. List objects are `Mutable` by nature, hence Python Lists can be altered even after their creation.

#### Example:
```
    stationaryItems = ["Pencil", "Eracers", "Pens", "Papers", "Exam Pads"]

    print("\nThe class type is : ", type(stationaryItems))

    print("\nThe Stationary items are: ", stationaryItems, end="\n")

    print("\nFirst Stationary item is: ", stationaryItems[0], end="\n")
```

### What are the different types of copy methods by System Design :
1. As per the System Design standards, we have two types of copy methods
    1. **Shallow Copy** :
        - Shallow copy is a process where `A new object of collection directly references the properties and behaviors of the existing collection object`.
        - In Shallow copy one object changes another reference object also changes
    2. **Deep Copy** :
        -

### What are Python Tuple :
- Similar to Lists
- Tuples are immutable - once created, we cannot altered.
- print the tuple using tuple constructor
    ```
        nums = (1, 2, 3, 4)
        print("\nDisplay the elements from the tuple are : ", tuple(nums), end="\n)
    ```
- If you want to do any modifications
    - change tuple into list
    - do the operations
    - change list to tuple

### Understanding `Sets` collection in Python:
1. A `Set` is Python collection with an "Un-ordered" collection of items.
2. Every element in the `Set` should be definitely
    - Unique
    - mutable
3. The elements in the `Set` collection are never associated with any index
4. Python `Set` collection is a `Non-indexed data cllection object`.
5. Denoted by `{}`
6. Print the data using `set constructor`.
- **Example**:
    ```
        stationaryItems = {"Pencil", "Eracers", "Pens", "Papers", "Exam Pads"}

        print("\nThe class type is : ", type(stationaryItems))

        print("\nThe Stationary items are: ", set(stationaryItems), end="\n")

    ```

### Understanding `Dictionaries` in Python:
1. `Dictionary` in Python is a collection type, which manages "Un-Ordered collection of data values".
2. `Dictionary` is used to store the data values in the format of `<Key : Value>` pairs.
- **Basic Syntax:**

    ```
    dictionaryObject = {
        <key1> : <value1>,
        <key2> : <value2>,
        <key3> : <value3>,
        .............
        <keyN> : <valueN>,
    }
    ```
- **Basic Illustration**

    ```
    employeeDictionary = {
        "firstName" : "John",
        "lastName" : "Roy",
        "age" : 32,
        "job" : "IT"
    }
    ```