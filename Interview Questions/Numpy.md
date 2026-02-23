### 1. What is Numpy and Key features ?
- Numpy (Numerical Python) is one of the most funcemental and widely used libraries for numerical computing in Python.
- Numpy is an open source library that enables efficient numerical computations, especially dealing with large datasets.
- **Key features** :
    - Multi-dimensional arrays
    - Broadcasting : Allow operations on arrays of different shapes
    - Vectoriation : Perform operations without loops
    - Memory Efficinecy : Numpy arrays more memory efficient than Python List, because it stores same type of elements in Contiguous memory blocks
    - Integration with other libraries : foundation for other pyhton libraries like Pandas, SciPy

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

### 4. Difference between Lista and Numpy ?
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

### 11. What is Random Function ?
- NumPy random functions generate pseudo-random numbers from uniform, normal, and discrete distributions and are widely used in ML, simulations, and testing.

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
    - ndarray.shape
    - ndarray.size
    - ndarray.dtype
    - ndarray.ndim
    - ndarray.itemsize
    - ndarray.nbytes
    - ndarray.T
    - ndarray.flags
    - ndarray.strides
    - ndarray.base
    - ndarray.real
    - ndarray.imag
    - ndarray.flat
    - ndarray.ctypes
    - ndarray.view()
    - ndarray.copy()
    - ndarray.tolist()
    - ndarray.data()

### 16. Understanding the concept of Indexing and Slicing in NumPy Arrays
- **Indexing** :
    - Indexing refers to accessing specific elements within the NumPy array
    - Indexing allows retrieving OR modifying the individual elements OR group of elements in an array
    - Indexing starts from 0, and Thereby increments by 1
    - NumPy arrays will provide `Negative Indexing` to access the elements from the end of the array
    - Basic syntax of indexing
        - `NumPyArray[indexNumber]`
- **Slicing** -
    - Slicing allows accessing a range of elements (Also called as Sub-Array) from a NumPy array
    - Slicing is done using a colon (:) notation
    - Basic syntax of slicing
        - `NumPyArray(start:stop:step)`
            - Start: The starting index (Inclusive)
            - Stop: The ending index (Exclusive)
            - Step: The increment between indices (default is 1)
