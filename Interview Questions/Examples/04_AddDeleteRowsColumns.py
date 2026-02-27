import pandas as pd
import numpy as np

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

""" Adding a new column to the DataFrame """

# Method 1 : Using assignment operator
df["City"] = ['New York', 'Los Angeles', 'Chicago']
print("DataFrame after adding a new column using assignment operator: \n", df)

# Method 2: Using insert() method to add a new column at a specific position
df.insert(3, "Email", ["alice@example.com", "bob@example.com", "charlie@example.com"])
print("\nDataFrame after adding a new column using insert() method: \n", df)

# Method 3: Using assign() method to add a new column
df = df.assign(Country = ["USA", "USA", "USA"])
print("\nDataFrame after adding a new column using assign() method: \n", df)

# Method 4: USing loc() to add a new column
df.loc[:, "Phone Number"] = ["123-456-7890", "987-654-3210", "555-555-5555"]
print("\nDataFrame after adding a new column using loc() method: \n", df)


""" Adding a new row to the DataFrame """

# Method 1: Using loc() to add a new row
new_row = [4, "David", 40, "david@gmail.com", "Nebraska", "USA", 1234567890]
df.loc[len(df)] = new_row
print("\nDataFrame after adding a new row using loc() method: \n", df)

# Method 2 : Using concat() method to add a new row
single_row = pd.DataFrame({
    'ID': [5],
    'Name': ['Eve'],
    'Age': [28],
    'Email': ['eve@example.com'],
    'City': ['Miami'],
    'Country': ['USA'],
    'Phone Number': [9876543210]
})
df = pd.concat([df, single_row], ignore_index=True)
print("\nDataFrame after adding a new row using concat() method: \n", df)

multiple_row = pd.DataFrame({
    'ID': [6, 7],
    'Name': ['Frank', 'Grace'],
    'Age': [32, 29],
    'Email': ['frank@example.com', 'grace@example.com'],
    'City': ['Boston', 'Seattle'],
    'Country': ['USA', 'USA'],
    'Phone Number': [1112223333, 4445556666]
})
df = pd.concat([df, multiple_row], ignore_index=True)
print("\nDataFrame after adding multiple rows using concat() method: \n", df)

# Method 3 :Adding rows with default values
df.loc[len(df)] = [8, "Default Name", 0, "test", "", "USA", 0]
print("\nDataFrame after adding a new row with default values: \n", df)

# Method 4 : Adding row using conditional logic
new_row_conditional = {
    'ID': 9,
    'Name': 'Conditional Name',
    'Age': 0,
    'Email': 'test',
    'City': 'Atlanta',
    'Country': 'USA',
    'Phone Number': 0
}
if new_row_conditional['Age'] > 25:
    df.loc[(len(df))] = new_row_conditional
    print("\nDataFrame after adding a new row using conditional logic: \n", df)
else :
    print("\nNew row not added due to age condition.")

# Method 5 : Adding rows with missing values
new_row_with_missing_values = {
    'ID': 10,
    'Name': 'Missing Value Name',
    'Email': 'missing@example.com',
    'Country': 'USA',
}
df.loc[len(df)] = new_row_with_missing_values
print("\nDataFrame after adding a new row with missing values: \n", df)

""" Deleting a column from the DataFrame """

# Method 1: Using drop() method to delete a column
df = df.drop(columns = ['Phone Number'])
print("\nDataFrame after deleting a column using drop() method: \n", df)

df = df.drop(columns = ["Country", "Email"])
print("\nDataFrame after deleting multiple columns using drop() method: \n", df)

# Method 2: Using del keyword to delete a column
del df["City"]
print("\nDataFrame after deleting a column using del keyword: \n", df)

""" Deleting a row from the DataFrame """
# Method 1: Using drop() method to delete a row by index
df = df.drop(8)
print("\nDataFrame after deleting a row using drop() method: \n", df)

df = df.drop([5, 6, 7])
print("\nDataFrame after deleting multiple rows using drop() method: \n", df)

# Method 2: using conditional logic to delete rows
df = df[df['Age'] <= 30]
print("\nDataFrame after deleting rows using conditional logic: \n", df)
