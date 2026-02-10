### 1. How Python code is executed internally?
When we run a Python program, the source code is first compiled into platform-independent bytecode. This bytecode is stored in the __pycache__ directory as .pyc files. Then the Python Virtual Machine executes the bytecode line by line. So Python is both compiled and interpreted.
```
.py file  →  Compilation  →  Bytecode (.pyc)  →  Python Virtual Machine  →  Output
```
### 2. Difference between CPython, PyPy, Jython?
- These are different implementations of Python (different engines that run Python code).
- **CPython** :
    - CPython is the default Python interpreter written in C and is most commonly used.
    - Python code → Bytecode → Python Virtual Machine (PVM)
- **PyPy** :
    - PyPy is an alternative implementation that uses JIT compilation to improve performance for long-running programs.
    - Python code → Bytecode → JIT → Machine code (optimized at runtime)
- **Jython** :
    - Jython is a Python implementation that runs on the JVM and is mainly used to integrate Python with Java-based systems.
    - Python code → Java Bytecode → JVM

### 3. What's the difference between shallow copy and deep copy when assigning variables in Python?
- Shallow copy creates a new outer object but shares inner references, so changing inner content affects the original, but replacing an inner object does not.
- Deep copy creates a completely independent copy, so changes do not affect the original at all.
- In Python, use `copy.copy()` for shallow copy and `copy.deepcopy()` for deep copy.

### 4. Explain variable scoping rules in Python (LEGB rule)
- LEGB is the order Python searches for variables :
    - Local
    - Enclosed (non-local)
    - Global
    - Built-in
- Python searches from innermost to outermost scope
- **Local Scope**
    - Variables defined inside the function
    - Accessible only inside that function
- **Enclosed Scope**
    - Variables defined in outer function has enclosed scope
    - not local, not global
- **Global Scope**
    - Variables defined at the module level (top-level in file)
    - Accessible inside functions using `global` if you want to modify them
- **Built-in Scope**
    - Ppre-denined names in python
    - len, max, min, dir
    - Accessible from anywhere

### 5. What happens when you assign a mutable object to multiple variables? How does this differ from immutable objects?
- When you assign a mutable object to multiple variables, all variables point to the same object, so modifying it via any variable affects all. For immutable objects, assignments initially point to the same object, but any modification creates a new object, leaving the original unchanged.
- Examples:
    - list, dict, set for mutable objects
    - int, str, float, tuple for immutable objects

### 6. What's the difference between is and ==? When would each fail unexpectedly?
- `==` : Equality
    - checks if the values of two objects are equal
    - Works for numbers, strings, lists, dicts, etc.
- `is`: Identity
    - checks whether two variables point to the same object in memory.
    - `is` can fail unexpectedly with integers > 256 or strings due to Python’s object caching
        ```
            a = 256
            b = 256
            print(a is b)  # True → same cached object
            print(a == b)  # True

            a = 257
            b = 257
            print(a is b)  # False → different objects in memory
            print(a == b)  # True
        ```
    - Never use `is` for numeric or string equality checks.
    - using `is` on mutable objects like lists or dicts can produce unexpected results.
    - Use `is` primarily for singletons like None

### 7. List vs Tuple vs Set
- These are built in datatypes in python, used to store the multiple elements of data.
- **List**
    - ordered (self-indexing feature)
    - Mutable
    - denoted by `[]`
    -  print data using list() constructor
- **Tuple**
    - ordered
    - immutable
    - denoted by `()`
    -  print data using tuple() constructor
    - If you want to do any modifications
        - change tuple into list
        - do the operations
        - change list to tuple
- **Set**
    - Unordered
    - unique data
    - mutable
    - denoted by `{}`
    - print data using set() constructor

### 8. Explain the internal implementation differences between lists and tuples. Why are tuples faster?
**List** :
- Implemented as a `dynamic array` in memory
- Characteristics :
    1. Mutable : can add/remove elements
    2. Over-allocated memory : Python allocates extra space to allow efficient appends
    3. Pointer-based : Each element is a reference to an object in memory
- Changing the list (like append/remove) may require resizing the array and copying elements → slight overhead.

**Tuple** :
- Implemented as a fixed-size array.
- Characteristics:
    1. Immutable: size and content cannot change
    2. No over-allocation: memory is allocated exactly for its elements
    3. Pointer-based: Each element is a reference, like lists
- Since tuples are fixed, Python can make them smaller and more memory-efficient

**Why tuples are faster than List**
| Reason | Explanation |
| -------- | ----------- |
| Immutability | Tuples cannot change size, so no overhead of dynamic resizing |
| Fixed memory allocation |	Python allocates exactly the memory needed for tuples, reducing memory operations |
| Simpler implementation | Tuples don’t need methods like append(), extend(), insert(), etc., so fewer function calls |
| Optimization by Python interpreter | Tuples can be used in places where a constant sequence is expected, allowing compiler-level optimizations |
| Cache-friendly | Smaller memory footprint → better CPU cache usage → faster iteration |

- Tuple operations are generally faster due to immutability and simpler memory layout
- Lists are implemented as dynamic arrays with extra memory allocation to allow appends, while tuples are fixed-size arrays. Tuples are faster because they are immutable, use less memory, have fewer operations, and allow the interpreter to optimize storage and access.

### 9. If tuples are immutable, how can they still contain mutable objects?
- Tuples are immutable
- But inner lists are mutable
    ```
        t = ([1,2], [3,4])
        t[0].append(5)   --> Allowed
    ```
- Tuple structure unchanged, contents inside mutable.

### 10. How do you handle large datasets that don't fit in memory? Compare different approaches
**Problem**
- When dataset size > available memory
    - Program crashes (outof memory)
    - Heavy swapping -> very slow
- So we use streaming, chunking, or distributed processing.

**Main Approaches**
1. Iterators & Generators (Streaming Processing)
    - Process data one record at a time instead of loading everything.
    - Very low memory usage and simple
    - works for logs, CSV, text files
    - Best for Log processing, ETL pipelines, Streaming APIs
2. Chunk Processing (Batching)
    - Read data in small chunks
    - Easy with Pandas
3. Memory-Mapped Files (mmap)
    - File stays on disk but accessed like memory
4. External Storage + Database
    - Store data in DB instead of RAM
        - PostgreSQL
        - MongoDB
        - ElasticSearch
5. Distributed Processing
    - Split dataset across multiple machines.
    - Tools
        - Spark
        - Hadoop
        - Dask

### 11. What happens when dictionary resizes?
- A dictionary (dict) is a built-in collection that stores data as key → value pairs.
- Mutable (you can add/remove)
- Keys must be : unique, immutable (string, int, tuple)
- Values can be any type
- Implemnted using a hash table
- When a Python dictionary becomes about two-thirds full, it resizes by creating a larger hash table and rehashing all existing keys into new slots. This reduces collisions and keeps lookup operations O(1) on average.

### 12. Difference between list vs tuple vs deque?
Lists are dynamic arrays that support fast indexing but slow insertions at the beginning. Tuples are immutable and more memory-efficient, making them slightly faster for fixed data. Deques are double-ended queues optimized for O(1) insertions and deletions from both ends, making them ideal for queues, stacks, and sliding window problems.

### 13. When to use set vs list?
Use a list when order and duplicates matter or when you need indexing. Use a set when you need fast membership checks, unique elements, or set operations like union and intersection. Sets provide O(1) average lookup, while lists require O(n) search.

### 14. If set is faster, why not always use set instead of list?
- We won't use Set always instead of List, because
    - No order
    - No indexing
    - Cannot store duplicates
    - Slightly more memory

### 15. Why keys in dict must be immutable?
- Dictionary keys must be immutable because Python uses the key’s hash to locate values. If the key changed after insertion, its hash would change and the dictionary wouldn’t be able to find it, breaking correctness.
- A hash is a unique (or almost unique) number used to quickly identify data.

### 16. Explain the difference between /, //, and how division behaves with negative numbers.
- `/` performs true division and always returns a float.
- `//` performs floor division, returning the largest integer less than or equal to the result.
- With negative numbers, Python rounds toward negative infinity, so -5 // 2 becomes -3, not -2.