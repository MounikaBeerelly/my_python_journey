## Full Function in Python:

### `np.full()` function:

1. The function `np.full()` is a part of the NumPy library in python, and it is used to create an array filled with a specified value
2. `np.full()` function allows the developer to generate arrays of any shape and type, initialized to constant value

#### Basic Syntax:
    `numpy.full(shape, fill_value, dtype=None, order='C)`

#### Parameters:

1. **Shape**: This parameter defines the shape of the output array. It can be an integer (for a 1D array) or a tuple(for multi-dimensional arrays)
2. **fill_value:** The value to fill the array with. This can be any scalar value
    - `e.g:` 0, 1, a string, etc.
3. **dtype (optional):** The data type of the resulting array. If not provided, the data type will be inferred from the fill_value
4. **order (optional):** It specifies the memory layout order.
    - `C` is for row-major (C-style) order,
    - `F` is for column-major (Fortan style) order.
    - By default is `C`