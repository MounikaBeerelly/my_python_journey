### 1. What is Numpy and Key features ?
- Numpy (Numerical Python) is one of the most funcemental and widely used libraries for numerical computing in Python.
- Numpy is an open source library that enables efficient numerical computations, especially dealing with large datasets.
- **Key features** :
    - Multi-dimensional arrays
    - Broadcasting : Allow operations on arrays of different shapes
    - Vectoriation : Perform operations without loops
    - Fast and efficient
    - Integration with other libraries : foundation for other pyhton libraries like Pandas, SciPy
    - Indexing and Slicing
    - Memory Management
- **Why NumPy is fast** :
1. Vectorization : No Python loops
    - In Python, operations run inside for loops
    - NumPy performs operations on entire array once using vectorized code.
        - Eliminates Python interprepreter overhead
        - Uses compiled C loops internally
        - Vectorized NumPy operations still use loops internally, but those loops run in optimized C with SIMD and cache-friendly memory access, eliminating Python interpreter overhead.
2. Contiguous memory layout : Stores data continuously without gaps/breaks
    - NumPy arrays store data in continuous memory blocks, unlike Python lists (which store references)
        - Fast memory access
        - Less memory overhead
        - Better CPU cache utilization
3. Homogeneous data types :
    - Python lists can store mixed types -> required type checking
    - NumPy arrays store single dtype -> no run time checking
4. Broadcasting : avoids data copies
    - NumPy can operate on arrays of different shapes without creating copies
    - Less memory usage
5. Implemented in C / Fortran (BLAS, LAPACK)
    - Core NumPy operations use highly optimized libraries:
        - BLAS → fast linear algebra
        - LAPACK → matrix decomposition
        - Vectorized CPU instructions (SIMD)
- **Why C is fast?**
    - C is a compiled language
    - Code is directly translated into CPU instructions before execution
    - No interpreter at runtime, direct CPU execution

### 2. Why Numpy is Important ?
1. Speed and Performance : NumPy is written in C, so it’s very fast
2. Handles large datasets like images or time-series data efficiently.
3. Foundation for Data science and ML : Many ML libraries are built on Numpy
4. NumPy supports a wide range of Mathematical and Statistical Operations
5. Easy of use : Simple syntax and structure

### 3. Why Numpy fast than Lists ?
- NumPy arrays are stored in contiguous blocks of memory, which allows for efficient access to elements.
- Vectorized Operations : eliminates the need for explicit loops in python
- Low level optimizations : built on C libraries
- Multithreading : large computations can be executed concurrently, utilizing multiple CPU cores, that speeding up the execution

### 4. Difference between Lists and Numpy ?
| Python Lists | NumPy Arrays |
| ------------ | ------------ |
| Heterogeneous : hold elements of different data types | Homogeneous : All elements must be of the same data type |
| Non-contiguous | Contiguous |
| Require explicit loops for elemet-wise operations | Vectorization |
| Slower Performance | Faster Performance |

### 5. Real-world applications of NumPy ?
1. Data Analysis
    - Used for data manipulation and numerical analysis.
    - Libraries like Pandas are bulit on top of NumPy arrays
2. Machine Learning
    - In Machine learning, NumPy arrays are used to
        - Represent datasets
        - Perform matrix operations
        - Optimize models
    - Popular ML frameworks like TensorFlow, Keras, and PyTorch utilize NumPy arrays for Tensor computation
3. scientific computing
    - Used in Physics, Chemistry, Biology, and Engineering for handling large datasets and complex math operations
4. Image Processing
    - Images are represented as 2D NumPy arrays of pixel values.
    - Enables tasks like filtering, edge detection, and transformations
5. Econometrics and Statistics
    - Efficient for matrix algebra, covariance calculations, and statistical tests on large datasets.

### 6. What is Broadcasting ?
- Ability to perform operations on arrays of different shapes
    ```
        a = np.array([1,2,3])
        b = 2
        print(a + b) # [3,4,5]
    ```
- Broadcasting rules
    - Dimensions equal OR
    - One dimension is 1

### 7. What is a NumPy Array?
- A NumPy array is often referred to as ndarray: N-dimesional array, which is a grid of values.
- All the values in an array should be of the same type
- Elements in NumPy array are indexed by a tuple of non-negative integers
- The number of dimensions and the shape of the array are defined by the user, making it highly flexible.
- NumPy arrays are multi-dimensional. A NumPy array can be
    - Single dimension : 1D called as vector
    - Two dimensions : 2D called as matrix
    - Three OR more dimensions : Higher-dimensional called as Tensor
- Once a NumPy array is created, its size cannot be changed. Which means elements cannot be added OR Removed, but the values in the array can be modified.
- Syntax : `numpy.array(object,dtype=none,copy=true,order='K',subok=False,ndmin=0)`
- We can create NumPy arrays using various methods. Here are some common ways to create NumPy arrays:
    - Using np. array()
    - np.zeros()
    - np.ones()
    - np.full()
    - np.arange()
    - np.linspace()
### 8. What is np.arange() function ?
- np.arange() : array range
- It means creating an array within a given range of values.
- It is based on the step size
- The `np.arange()` function in NumPy generates evenly spaced values within a specified interval, creating a 1D array.
- Syntax: `numpy.arange([start, ] stop,[step, ], stype=none)`
     **start**: (Optional) Starting a value of the sequence. Default is 0
    - **stop**: (required) End value of the sequence (exclusive)
    - **step**: (optional) Difference between consecutive values. Default is 1
    - **dtype**: (optional) Specifies the desired data type of the array. If not provided, it is inferred
### 9. What is reshape() function ?
- The reshape() function is used to change the shape (dimensions) of an array without changing its data.
```
    myArray01 = np.arange(1,13)
    print(f"\nPrinting the elements from the array01...",end="\n")
    print(myArray01)

    myArray02 = np.arange(1,13).reshape(3,4)
    print(f"\nPrinting the elements from the array02...",end="\n")
    print(myArray02)
```
### 10. What is linspace function ?
- The linspace() function creates an array of evenly spaced numbers between a start and stop value.
- It is based on the number of values, not step size
- Syntax : `numpy.linspace(start,stop,num=50, endpoint=True, restep=False, dtype=none, axis=0)`
    - **start**: The starting value of the sequence
    - **stop**: The ending value of the sequence
    - **num**: (Optional) The number of points to generate. Default is 50
    - **endpoint**: (Optional) If true (default), includes the stop value; otherwise, excludes it
    - **retstep**: (Optional) If True, returns the spacing between points along with the array
    - **dtype**: (Optional) specifies the desired data type of the output array
    - **axis**: (Optional) Axis in the result along which the values are stored
### 11. How to generate random numbers with NumPy?
- NumPy provides a wide range of functions for generating random numbers. You can generate random numbers from various probability distributions, set seeds for reproducibility and more.
- Here are some common ways to generate random numbers with NumPy:
1. Using np.random.rand()
    - Generating a Random Float between 0 and 1 using np.random.rand()
    - `random_float = np.random.rand()`
2. Using np.random.randint()
    - Generating a Random Integer within a Range using np.random.randint().
    - `random_integer = np.random.randint()`
3. Using np.random.randn()
    - `random_float = np.random.rand()`
4. Using np.random.seed()
    - We can set a seed using np.random.seed() to ensure that the generated random numbers are reproducible.
    - `np.random.seed(seed_value)`
### 12. What is Empty function ?
- The function `np.empty()` is a part of the NumPy library in python, and it is used to create an uninitialized array.
- Uninitialized array means that the contents of the array are not set to any specific value by the developer
- Uninitiallized array contain random or garbage values from memory
- Syntax: `numpy.empty(shape, dtype=float, order='C)`
    - **Shape**: A tuple the specifies the dimensions of the array.
        - For example: (2,3) would create a 2*3 array
    - **dtype (optional):** The desired data type for the array.
        - By default, it is float
        - You can specify other types like int,bool etc
    - **order (optional):** It specifies the memory layout order.
        - 'C' is for row-major (C-style) order,
        - 'F' is for column-major (Fortan style) order.
        - By default is 'C'
### 13. What is Full Function in Python?
- The function `np.full()` is a part of the NumPy library in python, and it is used to create an array filled with a specified value
- `np.full()` function allows the developer to generate arrays of any shape and type, initialized to constant value
- Syntax: `numpy.full(shape, fill_value, dtype=None, order='C)`
    - **Shape**: This parameter defines the shape of the output array. It can be an integer (for a 1D array) or a tuple(for multi-dimensional arrays)
    - **fill_value:** The value to fill the array with. This can be any scalar value
        - `e.g:` 0, 1, a string, etc.
    - **dtype (optional):** The data type of the resulting array. If not provided, the data type will be inferred from the fill_value
    - **order (optional):** It specifies the memory layout order.
        - `C` is for row-major (C-style) order,
        - `F` is for column-major (Fortan style) order.
        - By default is `C`

### 14. What is dtype attribute ?
- The dtype attribute stands for data type of the elements in a NumPy array.
- The dtype attribute defines the type of elements stored in the array, such as
    - integers
    - floating-point numbers
    - strings
    - user-defined types

### 15. Array attributes in Numpy?
- NumPy provides several array attributes, that typically provide information about the array's structure and memory layout.
- The list of Array attributes are:
    - `ndarray.shape` - returns array dimesions
    - `ndarray.size` - returns total number of elemnts
    - `ndarray.dtype` - returns datatype of elements
    - `ndarray.ndim` - returns number of dimensions
    - `ndarray.itemsize` - retuns size of each element (bytes)
    - `ndarray.nbytes` - total memory used
    - `ndarray.T` - Transpose of array
    - `ndarray.flags` - Memory layout info (C_CONTIGUOUS, OWNDATA, etc.)
    - `ndarray.strides` : Bytes to move in memory for next step in each dimension.
    - `ndarray.base` : Returns base array if view
    - `ndarray.real` : Real part of complex array
    - `ndarray.imag` : Imaginary part of complex array
    - `ndarray.flat` : Iterator over array elements
    - `ndarray.ctypes` : Gives C interface pointer
    - `ndarray.view()` : Creates view (shares memory)
    - `ndarray.copy()` : Creates deep copy
    - `ndarray.tolist()` : Convert to Python list
    - `ndarray.data()` : Pointer to raw memory buffer

### 16. Understanding the concept of Indexing and Slicing in NumPy Arrays
- **Indexing** :
    - Indexing refers to accessing specific elements within the NumPy array
    - Indexing allows retrieving OR modifying the individual elements OR group of elements in an array
    - Indexing starts from 0, and Thereby increments by 1
    - NumPy arrays will provide `Negative Indexing` to access the elements from the end of the array
    - Syntax : Uses square brackets with index values
        - `NumPyArray[indexNumber]`
        - e.g., arr[2], arr[1, 3]
- **Slicing** -
    - Slicing allows accessing a range of elements (Also called as Sub-Array) from a NumPy array
    - Slicing is done using a colon (:) notation
    - Syntax: Uses a colon (:) inside square brackets
        - `NumPyArray(start:stop:step)`
            - Start: The starting index (Inclusive)
            - Stop: The ending index (Exclusive)
            - Step: The increment between indices (default is 1)
            - e.g., arr[1:5]

### 17. How does NumPy handle memory?
NumPy handles memory efficiently using contiguous storage, homogeneous dtypes, views instead of copies, stride-based indexing, and broadcasting to avoid unnecessary memory allocation.
### 18. Explain views vs copies in NumPy ?
- `View` :
    - A view is another array object that shares the same memory as the original array.
    - Changing the view changes the original array.
    - Example
    ```
        import numpy as np

        arr = np.array([1, 2, 3, 4])
        view = arr[1:3]   # slicing creates a view

        view[0] = 99
        print(arr)   # original array changed

        Output
        ------
        [ 1 99  3  4]
    ```
    - Because both arrays point to the same memory block
- `Copy` :
    - A copy creates a new memory allocation
    - Changing the copy does NOT affect the original array
    - Example
    ```
        import numpy as np

        arr = np.array([1, 2, 3, 4])
        copy = arr[1:3].copy()

        copy[0] = 10
        print(arr)   # original unchanged
        print(copy)

        Output
        ------
        [ 1 99  3  4]
        [10  3]
    ```
### 19. How to optimize NumPy performance?
- Use Vectorization
- Choose right datatype
- Avoid unnecessary copies : Use views instead of copies
- Use in-place operations
- Leverage broadcasting : Broadcasting avoids creating temporary arrays
- Use built-in NumPy functions
### 20. How does NumPy achieve parallelism ?
NumPy achieves parallelism indirectly through vectorized operations and multi-threaded BLAS/LAPACK libraries that execute computations across CPU cores and SIMD units.
### 21. You have 10M rows — Python loop is slow. What do you do?
I avoid Python loops and use NumPy vectorization. If vectorization isn’t possible, I use Numba for JIT compilation or Dask for chunked/distributed processing.
### 23. What is __array_ufunc__ and why is it important?
- A ufunc (universal function) is a NumPy function that operates element-wise on arrays.
- `__array_ufunc__` is a special method (dunder method) that lets custom classes override how NumPy ufuncs behave.
    - Introduced in NumPy 1.13
    - Enables custom array-like objects to integrate with NumPy
### 24. Convert a multidimensional array to 1D array.
- Convert a multidimensional array to a 1D array which is also known as flattening the array in NumPy using various methods. Two common methods are using for the Convert a multidimensional array to 1D array.
1. Using flatten():
    ```
        # Create a multidimensional array
        multidimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ​
        # Use the flatten() method to convert it to a 1D array
        one_dimensional_array = multidimensional_array.flatten()
        ​
        print("one dimensional array", one_dimensional_array)

        Output:
        -------
        one dimensional array [1 2 3 4 5 6 7 8 9]
    ```
2. Using ravel():
    ```
        # Create a multidimensional array
        multidimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ​
        # Use the ravel() method to convert it to a 1D array
        one_dimensional_array = multidimensional_array.ravel()
        ​
        print("one dimensional array", one_dimensional_array)

        Output:
        -------
        one dimensional array [1 2 3 4 5 6 7 8 9]
    ```
- Both of these methods will flatten the multidimensional array into a 1D array. The primary difference between them:
    - Flatten() returns a new copy of the array. Any modifications in the flattened array do not affect the original array
    - Ravel() returns a flattened view of the original array whenever possible. Changes made to the raveled array may affect the original array since they share the same data in memory.

### 25. How do you sort a NumPy array in ascending or descending order?
- In NumPy, you can sort arrays using:
    - np.sort() → returns a sorted copy
    - array.sort() → sorts in-place
1. Sort in Ascending Order (Default) :
    - Using `np.sort()` : Original array remains unchanged.
        ```
            import numpy as np

            arr = np.array([5, 2, 9, 1, 7])
            sorted_arr = np.sort(arr)

            print(sorted_arr) # [1, 2, 5, 7, 9]
        ```
    - Using in-place sort : Modifies the original array
        ```
            arr.sort()
            print(arr)
        ```
2. Sort in Descending Order
- NumPy doesn’t have a direct descending flag, but you can reverse the ascending result.
    - Reverse slicing
        ```
            desc_arr = np.sort(arr)[::-1]
            print(desc_arr)
        ```
    - Using np.flip
        ```
            desc_arr = np.flip(np.sort(arr))
        ```
3. Sorting 2D arrays
    - Sort rows (axis = 1)
        ```
            arr2d = np.array([[3, 1, 2],
                              [9, 7, 8]])

            print(np.sort(arr2d, axis=1))

            Output:
            -------
            [[1 2 3]
             [7 8 9]]
        ```
    - Sort columns (axis = 0)
        ```
            print(np.sort(arr2d, axis=0))

             Output:
             -------
            [[3 1 2]
             [9 7 8]]
        ```
4. Sorting with Indices
    - np.argsort() → returns index positions
        ```
            arr = np.array([5, 2, 9, 1])
            indices = np.argsort(arr)

            print(indices)       # [3 1 0 2]
            print(arr[indices])  # [1 2 5 9]
        ```
    - Useful for:
        - ranking
        - sorting multiple arrays based on one array
        - interview scenarios

**Note** :
- np.sort() → copy
- array.sort() → in-place
- np.argsort() → returns sorted indices

### 26. Difference between np.reshape() and np.resize()
| Feature | reshape() | resize() |
| ------- | --------- | -------- |
| Definition | Returns a new view or copy of the array with a new shape | Modifies the array itself (in-place) to match the new shape |
| Original Array | Does not change the original array unless inplace modification is forced | 	Changes the original array directly |
| Return Value	| Returns the reshaped array (new object) |	Returns None (operation done in-place) |
| Data Handling | Requires that the total number of elements match the new shape |	If new size is bigger → fills with zeros. If smaller → array is trimmed |
| Memory | Often returns a view (shares data) if possible, else a copy | Creates/reallocates memory if needed |
| Use Case |	When you want a reshaped version of an array without altering the original | When you want to permanently change the shape of the array, even if padding or truncating is needed |

### 27. How to compare two NumPy arrays?
1. `Using == operator`
    - We generally use the == operator to compare two NumPy arrays to generate a new array object.
    - Call ndarray.all() with the new array object as ndarray to return True if the two NumPy arrays are equivalent.
    ```
        import numpy as np
        ​
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([1, 2, 3])
        arr3 = np.array([1, 4, 3])
        ​
        print((arr1 == arr2).all())  # True
        print((arr1 == arr3).all())  # False

        Output:
        -------
        True
        False
    ```
2. `Using array_equal()`
    - This array_equal() function checks if two arrays have the same elements and same shape.
    ```
        numpy.array_equal(arr1, arr2)
    ```
### 28. What is Vectorization in Numpy?
- Vectorization in NumPy means performing operations on entire arrays or vectors at once without using explicit loops. NumPy internally uses optimized C code, so vectorized operations are much faster than iterating through elements in Python.
- Eliminates the need for for loops.
- Operations are applied element-wise on the whole array.
- Improves performance and makes code more concise.
```
    import numpy as np
    ​
    # Without vectorization (using loop)
    arr = np.array([1, 2, 3, 4, 5])
    squared_loop = []
    for x in arr:
        squared_loop.append(x ** 2)
    print("Using loop:", squared_loop)
    ​
    # With vectorization
    squared_vectorized = arr ** 2
    print("Using vectorization:", squared_vectorized)
    Output:

    Using loop: [1, 4, 9, 16, 25]
    Using vectorization: [ 1  4  9 16 25]
```
### 29. What np.bincount() does
- Counts how many times each non-negative integer appears in the array.
- The index = number, value = frequency
- Counts step by step
```
    import numpy as np

    arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
    print(np.bincount(arr)) # [4 2 1 1 3 2 0 0 0 1]
```
### 30. How is vstack() different from hstack() in NumPy?
- Both methods are used for combining the NumPy arrays.
- The main difference is that the hstack method combines arrays horizontally whereas the vstack method combines arrays vertically.
- For example, consider the below code.
```
    import numpy as np
    a = np.array([1,2,3])
    b = np.array([4,5,6])

    # vstack arrays
    c = np.vstack((a,b))
    print("After vstack: \n",c)
    # hstack arrays
    d = np.hstack((a,b))
    print("After hstack: \n",d)
    The output of this code would be:

    After vstack:
    [[1 2 3]
    [4 5 6]]
    After hstack:
    [1 2 3 4 5 6]
```
