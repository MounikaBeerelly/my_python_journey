import pandas as pd
import numpy as np

""" converting dataframe to numpy array """

df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Method 1: Using the to_numpy() method
numpy_array = df.to_numpy()
print("DataFrame converted to NumPy array: \n", numpy_array)

# Method 2: Using the values attribute
numpy_array_values = df.values
print("\nDataFrame converted to NumPy array using values attribute: \n", numpy_array_values)


""" Converting dataframe to excel file """

df_to_excel = df.to_excel(r"C:\Practice\my-python-journey\Interview Questions\Examples\OutData\dataframeToExcel.xlsx")

print("\nDataFrame has been converted to an Excel file at the specified path.")


"""Accessing few records from a DataFrame"""

# Using head() method to access the first few records

df_head = df.head(2)
print("\nFirst 2 records of the DataFrame: \n", df_head)

# Using iloc() to access specific records by index

df_iloc = df.iloc[1:3]
print("\nRecords from index 1 to 2 using iloc: \n", df_iloc)

"""Selecting specific columns from a DataFrame"""

# using dot notation

selected_column_by_dot = df.Age
print("\nSelected column using dot notation: \n", selected_column_by_dot)

# using bracket notation
select_column_by_bracket = df["Name"]
print("\nSelected column using bracket notation: \n", select_column_by_bracket)

# using loc to select specific columns

selected_columns_by_loc = df.loc[:, ['ID', 'Name']]
print("\nSelected columns using loc: \n", selected_columns_by_loc)

# using iloc to select specific columns by index
selected_columns_by_iloc = df.iloc[:, 1]
print("\nSelected column using iloc: \n", selected_columns_by_iloc)

# selecting as Dataframe
selected_column_as_dataframe = df[['Age']]
print("\nSelected column as DataFrame: \n", selected_column_as_dataframe)


"""Rename columns in a DataFrame"""

# using rename() method
df_renamed = df.rename(columns = {"ID" : "User_ID"})
print("\nDataFrame with renamed column: \n", df_renamed)

# Using set_axis() method to rename columns
df_set_axis = df.set_axis(['User_ID', 'User_Name', 'User_Age'], axis=1)
print("\nDataFrame with renamed columns using set_axis: \n", df_set_axis)