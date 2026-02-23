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

### 6.
