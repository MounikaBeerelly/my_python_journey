## Understanding `ndarray.dtype` attribute:

1. The dtype attribute stands for data type of the elements in a NumPy array.
2. The dtype attribute defines the type of elements stored in the array, such as
    - integers
    - floating-point numbers
    - strings
    - user-defined types
3. The dtype sttribute is used for
    - `Efficient Memory Usage` - You can specify the exact size of elements (e.g., int8, float64) to optimize memory usage.
    - `Type-Specific operations` - Ensure correct operations for specific data types
    - `Data Interoperability` - Helps in working with structured or binary data where the type and size must match.
    - `Precision Control` - Allows you to control precision in computations (e.g., using float32 for limited precision to save memory)
    - `Structured Data` - Allows for creating arrays with fields (like columns in a table)
4. `Default Behavior`: NumPy determines the dtype automatically based on input data
    - **Example**:
    ```
    np.array([1,2,3]).dtype #output: dtype('int32') or dtype('int64') (depends on a system)
    np.array([1.5,2.3]).dtype #output: dtype('float64')
    ```
5. `Specifying dtype`: We can explicitly specify the dtype when creating an array using the dtype parameter
    - **Example**
        `np.array([1,2,3],dtype = 'float32)`
6. `Checking dtype`: Use .dtype to check the type of an existing array
    - **Example** :
    ```
    arr = np.array([1,2,3])
    print(arr.dtype) #output: stype('int32')
    ```

    ### Common data types
    1. Integer types:
        - int8
        - int16
        - int32
        - int64
    2. Floating-point types:
        - float16
        - float32
        - float64
    3. Complex types:
        - complex64
        - complex128
    4. Boolean:
        - bool
    5. Strings :
        - str
        - object
    6. Structured types:
        - custom fields using tuples
7. `Changing dtype`: Use .astype() to cast an array to different types
    - **Example**:
    ```
    arr = np.array([1,2,3], dtype='int32')
    arr_float = np.astype('float64')
    print(arr_float.dtype) #output: dtype('float64')