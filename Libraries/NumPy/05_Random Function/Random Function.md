# Random Function:

## Understanding the `np.random.random()` function:

1. The np.random.random() function generates random floating-point numbers uniformly distributed between 0.0 (inclusive) and 1.0 (exclusive)
2. The random numbers are drawn from a uniform distribution and are useful for
    - Simulations
    - Testing
    - Creating random datasets

### Basic Syntax:
    `np.random.random(size = none)`

1. **size:** Specifies the shape of the output array
    - If None (default), a single float is returned
    - If an integer is provided, a 1D array of that length is returned
    - If a tuple is provided, it creates an array with the specified shape

2. `np.random.random()` part of NumPy's random module, which provides a suite of random number generation functions


## Understanding the `np.random.rand()` function:

1. `np.random.random()` and `np.random.rand()` are similar but not the same
2. `np.random.random()`
    - Generates random numbers between 0 and 1, with the shape specified by the argument passed to it
    - When no arguments are passed it generates a single random value
3. `np.random.rand()` generates random numbers between 0 and 1, but it uses positional arguments to define the shape of the output array
    - `np.random.rand()` takes dimensions as arguments and creates an array with those dimensions filled with random floating-point numbers drawn from a uniform distribution over (0,1)

### Basic Syntax:
    `numpy.random.rand(d0,d1,...,dn)`

- d0,d1,..., dn: The dimensions of the output array. These are provided as positional arguments

**Note**:  If no arguments are passed, it generates a single random number

## Understanding the `np.random.normal()` function:

1. `np.random.normal()`function in NumPy is used to generate samples from a normal (Gaussian) distribution.

### Basic Syntax:
   `numpy.random.normal(loc = 0.0, scale = 1.0, size = None)`

**Parameters Info**:

1. `loc (float, optional)`:
    - The mean (center) of the normal distribution
    - Default : 0.0
2. `scale (float, optional)`:
    - The standard deviation (spread) of the normal distribution
    - Must be a positive number
    - Default: 1.0
3. `size (int or tuple of ints, optional)`:
    - The shape of the output array
    - If none, a single value is returned

### Waht exactly `np.random.normal()` returns?
    - A single value or an array of values sampled from the specified normal distribution

### Note:
1. A normal distribution is symmetric and characterized by two parameters.
    - Mean (loc) determines the center
    - Standard deviation (scale) determines the spread
2. The normal distribution has a bell-shaped curve most values are concentrated near the mean
3. The 68-95-99.7 rule applies
    - ~68% of the data falls within 1 standard deviation
    - ~95% of the data falls within 2 standard deviation
    - ~99.7% of the data falls within 3 standard deviation.

### Where exactly `np.random.normal()` is used?
    - Simulations to generate random noise
    - Machine learning to initialize weights
    - Statistical modeling and synthetic data generation