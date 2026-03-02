import pandas as pd
import numpy as np

# Create a sample DataFrame
dataframe = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 55000, 70000, 55000]
})

# Method 1: Sort by a single column (e.g., Age) using sort_values

sortData = dataframe.sort_values("Age") # ascending order by default
print("Sorted by Age:\n", sortData)

descendingSortData = dataframe.sort_values("Age", ascending=False) # descending order
print("\nSorted by Age (Descending):\n", descendingSortData)

# Method 2: Sort by multiple columns (e.g., Salary and Age)

mutliSortData = dataframe.sort_values(by=['Salary', 'Age'], ascending=[True, False]) # Sort by Salary first, then by Age
print("\nSorted by Salary and Age:\n", mutliSortData)

# Method 3: Sorting with missing values
dataframe_with_nan = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, 45],
    'Salary': [50000, 60000, np.nan, 70000, np.nan]
})

sorted_with_nan = dataframe_with_nan.sort_values(by = 'Age', na_position = 'first')
print("\nSorted with NaN values first:\n", sorted_with_nan)

# MEthod 4: Sorting using sort_index
sorted_by_index = dataframe.sort_index(ascending=False) # Sort by index in descending order
print("\nSorted by Index (Descending):\n", sorted_by_index)