import pandas as pd
import numpy as np

# Create a DataFrame from Lists

single_list = [1, 2, 3, 4, 5]
multiple_lists = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]

df_from_single_list = pd.DataFrame(single_list, columns=['Numbers'])
df_from_multiple_lists = pd.DataFrame(multiple_lists, columns=['ID', 'Name', 'Age'])

print("DataFrame from Single List: \n", df_from_single_list)
print("\nDataFrame from Multiple Lists: \n", df_from_multiple_lists)

# Create a DataFrame from a Dictionary
dict = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New York', 'Los Angeles', 'Chicago']
}

df_from_dict = pd.DataFrame(dict)
print("\nDataFrame from Dictionary: \n", df_from_dict)

# Create a DataFrame from a NumPy Array
numpy_array = np.array([[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]])
df_from_numpy_array = pd.DataFrame(numpy_array, columns=['ID', 'Name', 'Age'])
print("\nDataFrame from NumPy Array: \n", df_from_numpy_array)

# Create a datafra,e from list of dictionaries
list_of_dicts = [
    {'ID': 1, 'Name': 'Alice', 'Age': 25},
    {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 35}
]
df_from_list_of_dicts = pd.DataFrame(list_of_dicts)
print("\nDataFrame from List of Dictionaries: \n", df_from_list_of_dicts)

# Create Dataframe from Pandas Series
series1 = pd.Series([1, 2, 3], name='ID')
series2 = pd.Series(['Alice', 'Bob', 'Charlie'], name='Name')
series3 = pd.Series([25, 30, 35], name='Age')

df_from_series = pd.DataFrame({'ID': series1, 'Name': series2, 'Age': series3})
print("\nDataFrame from Pandas Series: \n", df_from_series)

#  Create a DataFrame from a CSV file
csv_file_path = r"C:\Practice\my-python-journey\DataSets\DeptDataSet.csv"

df_from_csv = pd.read_csv(csv_file_path)
print("\nDataFrame from CSV file: \n", df_from_csv)

df_from_csv_with_table = pd.read_table(csv_file_path, sep=',')
print("\nDataFrame from CSV file using read_table: \n", df_from_csv_with_table)

# create a DataFrame from an Excel file
excel_file_path = r"C:\Practice\my-python-journey\DataSets\Excel files\Pandas.xlsx"

df_from_excel = pd.read_excel(excel_file_path)
print("\nDataFrame from Excel file: \n", df_from_excel)

# Create dataframe fro json file
json_file_path = r"C:\Practice\my-python-journey\DataSets\JSON files\DeptDataSet.json"

df_from_json = pd.read_json(json_file_path)
print("\nDataFrame from JSON file: \n", df_from_json)