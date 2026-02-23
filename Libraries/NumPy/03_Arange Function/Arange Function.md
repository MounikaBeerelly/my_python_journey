## Arange Function:

### np.arange() function: array range
- It means creating an array within a given range of values.
1. The `np.arange()` function in NumPy generates evenly spaced values within a specified interval, creating a 1D array.

### Basic Syntax:
    `numpy.arange([start, ] stop,[step, ], stype=none)`

- **start**: (Optional) Starting a value of the sequence. Default is 0
- **stop**: (required) End value of the sequence (exclusive)
- **step**: (optional) Difference between consecutive values. Default is 1
- **dtype**: (optional) Specifies the desired data type of the array. If not provided, it is inferred

### Note:
- supports integer, float, or custom data types
- When we want to generate the array with higher value to low value we have to definitely supply the step value in negative. Else an empty array generated.
