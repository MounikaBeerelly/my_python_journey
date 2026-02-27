import pandas as pd
import numpy as np

# Create a Series from a list
list = [10, 20, 30, 40, 50]

series_from_list = pd.Series(list)
print("Series from list ...\n", series_from_list)

# Series from a dictionary
dict = {"Name" : {"John", "Alice", "Bob"},
        "City" : {"New York", "Los Angeles", "Chicago"}}

series_from_dict = pd.Series(dict)
print("\nSeries from dictionary ...\n", series_from_dict)

# Series from a scalar value
scalar_value = 100

series_from_scalar = pd.Series(scalar_value, index = ['x', 'y', 'z'])
print("\nSeries from scalar values... \n", series_from_scalar)

# Series from a NumPy array
arr = np.array(["A", "B", "C", "D", "E"])

series_from_numpy = pd.Series(arr)
print("\nSeries from NumPy array... \n", series_from_numpy)

# Series from another Series
series01 = pd.Series([1, 2, 3, 4, 5])

series02 = pd.Series(series01)
print("\nSeries from another Series... \n", series02)

# Series from range/sequence
series_from_range = pd.Series(range(10))
print("\nSeries from range/sequence... \n", series_from_range)

# Series using linspace function
series_from_linspace = pd.Series(np.linspace(5, 50, 5))
print("\nSeries from linspace function... \n", series_from_linspace)