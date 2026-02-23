## Understanding NumPy Arrays

1. NumPy arrays are the core data structure of the NumPy library
2. Understanding NumPy is fundemental to working efficiently with numerical data in Python
3. NumPy arrays provide High-performance, Multi-dimensional data structures optimized for numerical computations.

## What is a NumPy Array?

1. A NumPy array is often referred to as ndarray: N-dimesional array, which is a grid of values.
2. All the values in an array should be of the same type
3. Elements in NumPy array are indexed by a tuple of non-negative integers
4. The number of dimensions and the shape of the array are defined by the user, making it highly flexible.

## How many dimensions are supported by NumPy Arrays?

1. NumPy arrays are multi-dimensional
2. A NumPy array can be
    1. Single dimension : 1D called as vector
    2. Two dimensions : 2D called as matrix
    3. Three OR more dimensions : Higher-dimensional called as Tensor

## Note:

1. fixed size
    - Once a NumPy array is created, its size cannot be changed. Which means elements cannot be added OR Removed, but the values in the array can be modified.

2. Homogeneous
    - All elements in a NumPy array must have the same data type, making it more memory-efficient than Python lists.

### `np.array()` function:

1. `np.array()` function is the primary method for creating NumPy arrays
2. `np.array()` converts python sequences like lists, tuples, or other array-like structures into NumPy arrays, which provide enhanced functionality of numerical computation

### Basic Syntax:

    `numpy.array(object,dtype=none,copy=true,order='K',subok=False,ndmin=0)`

#### Parameters Info:
1. **Object**: The input data(list,tuple,or other array-like object) to be converted into an array
2. **dtype**: (Optional) Specifies the desired data type for the array. If not provided, it is inferred from the input data
3. **copy**: (Optional) If true, creates a copy of the object. If False, a view of the object may be created
4. **order**: (optional) Specifies the memory layout. 'C' for row-major (c-style), 'F for column-major (Fortan-style), and 'K' for preserving the input order
5. **subok**: (Optional) If true, sub-classes of ndarray are passed through; otherwise, the base class is used
6. **ndmin**: (optional) specifies the minimum number of dimensions the array should have. If the input data has fewer dimensions, new axes are prepended.
