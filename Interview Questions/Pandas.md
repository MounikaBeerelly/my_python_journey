### 1. What is Pandas ?
- Pandas is an open-source Python library used for data manipulation and analysis
- It works with structured data (tables, CSV, Excel, sQL, etc,.)
- Pandas most commonly used for data science, data analysis, and machine learning tasks
- **Why Pandas is important ?**
    - Easy data loading : supports multiple formats
    - Powerful data cleaning : Pandas drops the duplicate values, null values
    - Fast data manipulation : Filter, sort and transform data easily. Vectorized operations -> fast execution
    - SQL-like operations : Similar to SQL joins and aggregations
    - Provides time-series functionality : Used in finance, IoT, analytics
    - Integration with Data Science ecosystem
        - NumPy
        - Matplotlib
        - PySpark
        - TensorFlow
- **Why Pandas is Popular in Industry** :
    - Simple API
    - Handles large datasets efficiently
    - Built on fast NumPy arrays
    - Huge community support

### 2. What are the Different Types of Data Structures in Pandas?
- The two data structures that are supported by Pandas are Series and DataFrames.
1. `Series` :
    - Series is a one-dimensional labelled array that can hold data of any type.
    - Series data structure is can be considered like a column in an excel sheet
    - The key points to note about series are
        - Can manage homogeneous data
        - The size of the Series is immutable
        - The values of data in Series is mutable
    - A series can be created from a Python tuple, list and dictionary.
    - Axis labels are indexes.
2. `DataFrame`
    - DataFrame is a two-dimensional heterogeneous data structure.
    - It stores data in a tabular form.
    - The size of the dataframe is mutable.
    - The Panadas dataframe potentially manages Heterogeneous tabular data with labelled axes represented as Rows and Columns.
    - Pandas dataframe consists of three principal components
        - Data
        - Rows
        - Columns
### 3. What are the Different Ways to Create a Series?
- In Pandas, a series can be created in many ways. They are as follows:
1. Creating a Series from a List
    - We can create a series using a Python list and pass it to the Series() constructor.
    ```
        import pandas as pd

        s = pd.Series([10, 20, 30])
        print(s)
    ```
    - Pandas automatically assigns index 0, 1, 2
2. From List with Custom Index
    - Create a Series using Python List and pass the custom indexes
    ```
        s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    ```
3. Creating a Series from Dictionary :
    - Create a Series using Python dictionary and pass it to the Series constructor. The keys of the dictionary are become indexes and values becomes data.
    ```
        import pandas as pd

        dict = {'Geeks': 10,'for': 20, 'geeks': 30}

        print(pd.Series(dict))
    ```
4. From a Scalar Value :
    - Creates Series with repeated value.
    ```
        s = pd.Series(5, index=["a", "b", "c"])
    ```
5. From NumPy Array
    ```
        import numpy as np

        arr = np.array([1,2,3])
        s = pd.Series(arr)
    ```
    - Fast because uses NumPy internally
6. From Another Series (Copy)
    - Useful when modifying without affecting original
    ```
        s1 = pd.Series([1,2,3])
        s2 = pd.Series(s1)
    ```
7. From Range / Sequence
    ```
        s = pd.Series(range(5))
    ```
8. Creating a Series using NumPy Functions :
    - The Numpy module's functions, such as numpy.linspace() and numpy.random.randn() can also be used to create a Pandas series.
    ```
        import pandas as pd
        import numpy as np

        ser1 = pd.Series(np.linspace(3, 33, 3))
        print(ser1)

        ser2 = pd.Series(np.random.randn(3))
        print("\n", ser2)
    ```
### 4. What are the Different ways to Create a DataFrame in Pandas?
- In Pandas, a dataframe can be created in many ways. They are as follows:
1. Creating a DataFrame using a List
    - Pass the list to the DataFrame() constructor.
    ```
        import pandas as pd

        lst = ['Geeks', 'For', 'Geeks', 'is',
        'portal', 'for', 'Geeks']

        print(pd.DataFrame(lst))
    ```
2. Creating a DataFrame using a Dictionary :
    - Pass the dictionary to the DataFrame() constructor.
    - The Keys of the dictionary will be the column names and the values of the dictionary are the data of the DataFrame.
    ```
        import pandas as pd

        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}

        print(pd.DataFrame(data))
    ```
3. Creating a DataFrame using a List of Dictionaries
    - Pass the list of dictionaries to the Dataframe constructor.
    - Each dictionary represents a row.
    ```
        data = [
            {"name": "A", "age": 25},
            {"name": "B", "age": 30}
        ]

        df = pd.DataFrame(data)
    ```
4. Creating a DataFrame from Pandas Series
    ```
        s1 = pd.Series([1,2,3])
        s2 = pd.Series([4,5,6])

        df = pd.DataFrame({"A": s1, "B": s2})
    ```
5. From CSV File
    ```
        df = pd.read_csv("file.csv")
    ```
6. From Excel File
    ```
        df = pd.read_excel("file.xlsx")
    ```
7. From JSON
    ```
        df = pd.read_json("file.json")
    ```
8. From SQL Database
    ```
        import sqlite3

        conn = sqlite3.connect("db.sqlite")
        df = pd.read_sql("SELECT * FROM table", conn)
    ```
### 5. How to Read Data into a DataFrame from a CSV file?
- We can create a data frame from a CSV (Comma Separated Values) file by using the read_csv() method which takes the csv file as the parameter.
    - `pandas.read_csv(file_name)`
- Another way to do this is by using the read_table() method which takes the CSV file and a delimiter value as the parameter.
    - `pandas.read_table(file_name, delimiter)`
### 6. How can a DataFrame be Converted to an Excel File?
- A Pandas DataFrame can be exported to Excel using `df.to_excel()`, supporting options like sheet names, multiple sheets, column selection, formatting, and appending.
- `DataFrame.to_excel(file_name)`
```
    import pandas as pd

    df = pd.DataFrame({
        "name": ["A", "B"],
        "age": [25, 30]
    })

    df.to_excel("data.xlsx")
```
### 7. How to Convert a DataFrame into a Numpy Array?
- Pandas dataframe converted to a NumPy array using the `to_numpy()` method.
```
    import pandas as pd

    df = pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })

    arr = df.to_numpy()
    print(arr)

    Output:
    ------
    [[1 3]
     [2 4]]
```
- We can also use `.values` to convert dataframe values to NumPy array
```
    arr = df.values
```
### 8. How to access the first few rows of a dataframe?
- The first few records of a dataframe can be accessed by using the pandas `head()` method. It takes one optional argument n, which is the number of rows. By default, it returns the first 5 rows of the dataframe.
```
    df.head(n)
```
- Another way to do it is by using `iloc()` method. It is similar to the Python list-slicing technique.
```
    df.iloc[:n]
```
### 9. How to Select a Single Column of a DataFrame?
There are many ways to Select a single column of a dataframe. They are as follows:
1. Using Bracket Notation (Most Common)
    ```
        import pandas as pd

        df = pd.DataFrame({
            "name": ["A", "B", "C"],
            "age": [20, 25, 30],
            "city": ["NY", "LA", "SF"]
        })

        col = df["age"]
        print(col)
    ```
    - Returns a Series
2. Using Dot Notation (Only if column name is valid identifier)
    ```
        col = df.age
    ```
3. Using .loc[] : Useful when selecting rows + columns together
    ```
        col = df.loc[:, "age"]

        df.loc[0:1, "age"]
    ```
4. Using .iloc[] (Position Based) : Selects the column by index position
    ```
        col = df.iloc[:, 1]
    ```
5. Selecting as DataFrame (Double Brackets)
    ```
        col_df = df[["age"]]
    ```
    - Returns a DataFrame, not Series
    - Useful when chaining operations
### 10. How to Rename a Column in a DataFrame?
1. Using rename()
    ```
        import pandas as pd

        df = pd.DataFrame({
            "name": ["A", "B"],
            "age": [20, 25]
        })

        df = df.rename(columns={"age": "Age"}) # Rename single column

        print(df)

        df = df.rename(columns={
            "name": "Name",
            "age": "Age"
        }) # Rename multiple columns
    ```
2. Rename with inplace=True
    ```
        df.rename(columns={"age": "Age"}, inplace=True)
    ```
    - Modifies original DataFrame
3. Rename Using set_axis()
    ```
        df = df.set_axis(["Name", "Age"], axis=1)
    ```
### 11. How to add Row or Column to an Existing Dataframe?
**Adding Column to the Dataframe**
1. `By declaring a new list or dictionary as column`
    - First create dataframe
    - Add new column to the DataFrame by with the list of values.
    - Length of the list should be equal to the length of index column, else it will show error.
        ```
            import pandas as pd

            # Define a dictionary containing Students data
            data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
                    'Height': [1, 2, 3, 4],
                    'Qualification': ['A', 'B', 'C', 'D']}

            # Convert the dictionary into DataFrame
            df = pd.DataFrame(data)

            # Declare a list that is to be converted into a column
            address = ['NewYork', 'Chicago', 'Boston', 'Miami']

            # Using 'Address' as the column name
            # and equating it to the list
            df['Address'] = address

            display(df)
        ```
    - Using list for adding column will modify the existing dataframe.
2. `Using DataFrame.assign() method`
    - Adding New Column with assign() method creates a new DataFrame with the specified column(s) added.
    - The original DataFrame remains unchanged unless we explicitly reassign the result back to it.
    ```
        import pandas as pd

        # Define a dictionary containing Students data
        data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}

        # Convert the dictionary into DataFrame
        df = pd.DataFrame(data)

        # using assign() and passing address list as parameter
        df = df.assign(address = ['NewYork', 'Chicago', 'Boston', 'Miami'])

        print(df)
    ```
    - We can also use assign() method for adding Multiple columns at the same time by passing multiple key-value pairs (where the key is the column name and the value is the column data). It returns a new DataFrame, leaving the original one unchanged. We can achieve that using dictionary unpacking.
    ```
        #example -  add both "Age" and "City" columns
        new_columns = {'Age': [21, 22, 23, 24],
                    'City': ['NY', 'LA', 'SF', 'DC']}

        # unpacks new_columns dictionary and adds both "Age" and "City"
        df = df.assign(**new_columns)
        print(df)
    ```
3. `using DataFrame.insert()`
    - insert() method modifies the original dataframe, so there’s no need to reassign the DataFrame after using it.
    - add a column at any position and not just at the end.
    It also provides different options for inserting the column values.
    ```
        import pandas as pd

        # Define a dictionary containing Students data
        data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
                'Height': [1, 2, 3, 4],
                'Qualification': ['A', 'B', 'C', 'D']}

        # Convert the dictionary into DataFrame
        df = pd.DataFrame(data)

        # Using insert() to add a column at position 2 (3rd column)
        df.insert(2, "Age", [21, 23, 24, 21], True)
        print(df)
    ```
4. `using Dataframe.loc()`
    - Using .loc[], you can add a new column directly or modify values based on conditions, or when adding new columns based on specific row selections.
    ```
        import pandas as pd
        ​
        # dictionary containing Students data
        data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
                'Height': [1, 2, 3, 4],
                'Qualification': ['A', 'B', 'C', 'D']}
        ​
        # Convert the dictionary into DataFrame
        df = pd.DataFrame(data)
        ​
        # Using .loc[] to add a "Category" column
        # based on height condition
        df.loc[df['Height'] >= 3, 'Category'] = 'Tall'
        df.loc[df['Height'] < 3, 'Category'] = 'Short'
        ​
        # Observe the result
        print(df)
    ```
**Adding row to the Dataframe :**
1. `Using loc[] - By Specifying its Index and Values`
    - The loc[] method is directly modifying an existing DataFrame
    ```
        import pandas as pd
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
        df = pd.DataFrame(data)

        # Add a new row using loc[]
        df.loc[len(df)] = ["Charlie", 35]
        print(df)
    ```
2. `Adding Row Using concat()`
    - The concat() function merges two DataFrames along rows (or columns).
    - To add a single row, create it as a DataFrame and concatenate it with the original.
    - Ideal for adding multiple rows or when working with external data sources.
    - It avoids modifying the original DataFrame directly.
    ```
        import pandas as pd
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
        df = pd.DataFrame(data)
        ​
        # single row
        new_row = pd.DataFrame({"Name": ["Eve"], "Age": [28]})
        df = pd.concat([df, new_row], ignore_index=True)
        print(df)

        # Multiple rows as a DataFrame
        new_rows = pd.DataFrame({"Name": ["Charlie", "Diana"], "Age": [35, 28]})
        df = pd.concat([df, new_rows], ignore_index=True)
        print(df)
    ```
3. `Adding a Row with Default Values`
    - When you need to add a placeholder row with default values for further updates or processing.
    ```
        import pandas as pd
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
        df = pd.DataFrame(data)
        ​
        # Add a placeholder row
        df.loc[len(df)] = ["Unknown", 0]
        print(df)
    ```
4. `Adding Rows Conditionally`
    - Adding rows only if certain conditions are met.
    ```
        import pandas as pd
        data = {"Employee": ["Alice", "Bob"], "Salary": [5000, 6000]}
        df = pd.DataFrame(data)
        ​
        # Add a row only if the salary is below a threshold
        if df["Salary"].max() < 7000:
            df.loc[len(df)] = ["Charlie", 7000]
        print(df)
    ```
5. `Adding Rows with Missing Columns`
    - Handling scenarios where the new row has fewer columns than the original DataFrame.
    ```
        import pandas as pd
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30], "City": ["NY", "LA"]}
        df = pd.DataFrame(data)
        ​
        # Add a row missing one column
        new_row = {"Name": "Charlie", "Age": 35}  # No "City"
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        print(df)
    ```
### 12. How to Delete an Row or Column from an Existing DataFrame?
In Pandas, deleting rows or columns from a DataFrame is usually done using the drop() method.

**Delete a Column**
1. `Using drop() method`
    - Drop single column
    ```
        import pandas as pd

        df = pd.DataFrame({
            "name": ["A", "B", "C"],
            "age": [20, 25, 30],
            "salary": [30000, 40000, 50000]
        })

        df = df.drop("salary", axis=1)
        print(df)
    ```
    - Drop multiple columns
    ```
        df = df.drop(["age", "salary"], axis=1)
    ```
    - Delete column using inplace=True : modifies original dataframe
    ```
        df.drop("salary", axis=1, inplace=True)
    ```
2. `Delete Using del (Column Only)`
    ```
        del df["salary"]
    ```
**Delete a Row**
1. `Using drop() method`
    - Delete row by index
        ```
            df = df.drop(1)
        ```
    - Delete multiple rows
    ```
        df = df.drop([0, 2])
    ```
    - Delete row with inplace=True
    ```
        df.drop(1, inplace=True)
    ```
2. `Delete Rows Based on Condition`
    ```
        df = df[df["age"] > 22]
    ```
    - Keeps rows matching condition
    - Indirect way to delete rows
### 13. How to Merge Two DataFrames?
- In Pandas, merging DataFrames is used to combine data from multiple tables (just like SQL joins).
- The main function to merge two dataframes is `pd.merge()`
1. **Using `concat()` to Combine DataFrames**
    - The concat() function allows you to stack DataFrames by adding rows on top of each other or columns side by side.
    - Stacking DataFrames Vertically
    ```
        import pandas as pd
        ​
        df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Age': [35, 40]})
        ​
        c_df = pd.concat([df1, df2])
        ​
        print(c_df)

        # The indexes are not reset. Use ignore_index=True for clean indexes
        combinedf = pd.concat([df1, df2], ignore_index=True)
        print(combinedf)
    ```
    - Stacking DataFrames Horizontally
    ```
        df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        df2 = pd.DataFrame({'City': ['New York', 'Los Angeles'], 'Salary': [70000, 80000]})

        c_df = pd.concat([df1, df2], axis=1)

        print(c_df)
    ```
2. **Using `merge()` to combine dataframes**
    - The merge() Function is like joining tables in SQL. It combines DataFrames based on common columns or indexes.
    1. Basic Merge (Inner Join)
        - Keeps only matching rows
        ```
            import pandas as pd

            df1 = pd.DataFrame({
                "id": [1, 2, 3],
                "name": ["A", "B", "C"]
            })

            df2 = pd.DataFrame({
                "id": [1, 2, 4],
                "salary": [30000, 40000, 50000]
            })

            merged = pd.merge(df1, df2, on="id")
            print(merged)
        ```
    2. Outer Join
        - Keeps all rows from both DataFrames
        - Missing values filled with NaN
        ```
            merged = pd.merge(df1, df2, on="id", how="outer")
        ```
    3. Left Join
        - Keeps all rows from left DataFrame and matching rows from right
        - Missing values become NaN
        ```
            merged = pd.merge(df1, df2, on="id", how="left")
        ```
    4. Right Join
        - Keeps all rows from right DataFrame and matching rows from left
        - Missing values become NaN
        ```
            merged = pd.merge(df1, df2, on="id", how="outer")
        ```
    5. Merge on Different Column Names
        - Useful when column names differ
        ```
            merged = pd.merge(df1, df2, left_on="emp_id", right_on="id")
        ```
    6. Merge on Multiple Columns
        - Similar to composite key joins
        ```
            merged = pd.merge(df1, df2, on=["id", "dept"])
        ```
    7. Merge Using Index
        - Used when index represents key
        ```
            merged = pd.merge(df1, df2, left_index=True, right_index=True)
        ```
- **When to Use: concat() vs merge()**
    - concat():
        - When you want to stack DataFrames (add rows or columns).
        - When the DataFrames have similar structures.
    - merge():
        -   When you need to join DataFrames based on shared columns or indices.
        - When you need different types of joins (inner, outer, etc.).
### 14. merge() vs join() vs concat()
| Feature | merge()	| join() | concat() |
| ------- | ------- | ------ | -------- |
| Purpose	| SQL-style join | Index join | Stacking data |
| Key-based join | Yes	| Mostly index	| No |
| Flexibility	| Most flexible | Medium | Simple stacking |
| Axis control | Column-based |	Index-based	| Row or column |
| Common use | Relational data | Index alignment | Append data |
### 15. How to sort a Dataframe ?
In Pandas, sorting a DataFrame is mainly done using:
1. **sort_values()** → sort a dataframe by one or more columns in either ascending or descending order
    1. `Sorting a dataframe by single row` :
        - The sort_values() method in Pandas makes it easy to sort our DataFrame by a single column. By default, it sorts in ascending order.
        ```
            import pandas as pd
            data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 30, 35, 40],
                    'Score': [85, 90, 95, 80]}
            df = pd.DataFrame(data)

            sorted_df = df.sort_values(by='Age') # Ascending order
            print(sorted_df)

            sorted_df = df.sort_values(by='Age',ascending=False) # descending order
        ```
    2. `Sorting a DataFrame by Multiple Columns` :
        ```
            import pandas as pd
            data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 30, 35, 40],
                    'Score': [85, 90, 95, 80]}
            df = pd.DataFrame(data)

            sorted_df = df.sort_values(by=['Age', 'Score'])
            print(sorted_df)
        ```
        - This will sort first by Age and if multiple rows have the same Age, it will then sort those rows by Salary.
    3. `Sorting DataFrame with Missing Values` :
        - By default sort_values() places NaN values at the end. If we need them at the top, we can use the na_position parameter.
        ```
            import pandas as pd
            data_with_nan = {"Name": ["Alice", "Bob", "Charlie", "David"],"Age": [28, 22, None, 22]}
            df_nan = pd.DataFrame(data_with_nan)

            sorted_df = df_nan.sort_values(by="Age", na_position="first")
            print(sorted_df)
        ```
        - Any rows with missing values in the Age column are placed at the top of the DataFrame.


2. **sort_index()** → sort by index
    1. `Sort by index` :
        - sort_index() sorts the DataFrame based on the index in ascending order
        ```
            import pandas as pd
            data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 30, 35, 40],
                    'Score': [85, 90, 95, 80]}
            df = pd.DataFrame(data)

            df_sorted_by_index = df.sort_index()
            print(df_sorted_by_index)
        ```
    - `Sort in descending order`:
        - sort by index in descending order by passing the ascending=False argument.
        ```
            import pandas as pd
            data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 30, 35, 40],
                    'Score': [85, 90, 95, 80]}
            df = pd.DataFrame(data)
            df_sorted_by_index_desc = df.sort_index(ascending=False)
            print(df_sorted_by_index_desc)
        ```
### 16. How to Check and Remove Duplicate Values in Pandas.
- In Pandas, duplicate values can be checked by using the `duplicated()` method.
    ```
        DataFrame.duplicated()
    ```
- To remove duplicate values, use drop_duplicates() method.
    ```
        DataFrame.drop_duplicates()
    ```
- The drop_duplicates() method in Pandas is designed to remove duplicate rows from a DataFrame based on all columns or specific ones. By default, it scans the entire DataFrame and retains the first occurrence of each row and removes any duplicates that follow.
    ```
        import pandas as pd

        data = {
            "Name": ["Alice", "Bob", "Alice", "David"],
            "Age": [25, 30, 25, 40],
            "City": ["NY", "LA", "NY", "Chicago"]
        }

        df = pd.DataFrame(data)

        print("Original DataFrame:")
        print(df)

        df_cleaned = df.drop_duplicates()

        print("\nModified DataFrame (no duplicates)")
        print(df_cleaned)
    ```
1. `Dropping Duplicates Based on Specific Columns`
    - Remove the duplicates in specific columns using the subset parameter.
    ```
        import pandas as pd
        ​
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'David'],
            'Age': [25, 30, 25, 40],
            'City': ['NY', 'LA', 'SF', 'Chicago']
        })
        ​
        df_cleaned = df.drop_duplicates(subset=["Name"])
        ​
        print(df_cleaned)
    ```
2. `Keeping the Last Occurrence of Duplicates`
    - By default drop_duplicates() retains the first occurrence of duplicates. If we want to keep the last occurrence we can use keep='last'.
    ```
        import pandas as pd
        ​
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'David'],
            'Age': [25, 30, 25, 40],
            'City': ['NY', 'LA', 'NY', 'Chicago']
        })
        ​
        df_cleaned= df.drop_duplicates(keep='last')
        print(df_cleaned)
    ```
3. `Dropping All Duplicates`
    - If we want to remove all rows that are duplicates, we can set keep=False.
    ```
        import pandas as pd
        ​
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'David'],
            'Age': [25, 30, 25, 40],
            'City': ['NY', 'LA', 'NY', 'Chicago']
        })
        df_cleaned = df.drop_duplicates(keep=False)
        print(df_cleaned)
    ```
4. `Modifying the Original DataFrame Directly`
    - If we want to modify the DataFrame in place without creating a new DataFrame set inplace=True.
    ```
        import pandas as pd
        ​
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'David'],
            'Age': [25, 30, 25, 40],
            'City': ['NY', 'LA', 'NY', 'Chicago']
        })
        df.drop_duplicates(inplace=True)
        print(df)
    ```
### 17. How to Handle Missing Data in Pandas?
- Handling missing data (NaN / None) is a core step in data cleaning with Pandas.
- Pandas provides powerful methods to detect, remove, and fill missing values.
- **Checking Missing Values in Pandas**
    1. Using isnull()
        - isnull() returns True for NaN values or null values and False for present values
        ```
            import pandas as pd
            import numpy as np

            d = {'First Score': [100, 90, np.nan, 95],
                    'Second Score': [30, 45, 56, np.nan],
                    'Third Score': [np.nan, 40, 80, 98]}
            df = pd.DataFrame(d)

            mv = df.isnull()

            print(mv)
        ```
    2. Using isna()
        - isna() returns True for NaN values or null values and False for present values
        ```
            import pandas as pd
            import numpy as np

            data = {'Name': ['Amit', 'Sita', np.nan, 'Raj'],
                    'Age': [25, np.nan, 22, 28]}

            df = pd.DataFrame(data)

            # Check for missing values using isna()
            print(df.isna())
        ```
- **Filling missing values**
1. `using fillna()` : fillna() used to replace missing values (NaN) with a given value.
    1. `Fill Missing Values with Zero`
        ```
            import pandas as pd
            import numpy as np

            d = {'First Score': [100, 90, np.nan, 95],
                    'Second Score': [30, 45, 56, np.nan],
                    'Third Score': [np.nan, 40, 80, 98]}
            df = pd.DataFrame(d)

            df.fillna(0)
        ```
    2. `Fill with Previous Value (Forward Fill)`
        - The pad method is used to fill missing values with the previous value.
        ```
            df.fillna(method='pad')
        ```
    3. `Fill with Next Value (Backward Fill)`
        - The bfill function is used to fill it with the next value.
        ```
            df.fillna(method='bfill')
        ```
2. `using replace()` : Use replace() function to replace NaN values with a specific value.
    ```
        df.replace(np.nan, 0)
    ```
- **Droping Missing values** : The dropna() function used to removes rows or columns with NaN values. It can be used to drop data based on different conditions.
1. `Dropping Rows with At Least One Null Value`
    - Remove rows that contain at least one missing value.
    ```
        import pandas as pd
        import numpy as np

        dict = {'First Score': [100, 90, np.nan, 95],
                'Second Score': [30, np.nan, 45, 56],
                'Third Score': [52, 40, 80, 98],
                'Fourth Score': [np.nan, np.nan, np.nan, 65]}
        df = pd.DataFrame(dict)

        df.dropna()
    ```
2. `Dropping Rows with All Null Values`
    - We can drop rows where all values are missing using dropna(how='all').
    ```
        dict = {'First Score': [100, np.nan, np.nan, 95],
                'Second Score': [30, np.nan, 45, 56],
                'Third Score': [52, np.nan, 80, 98],
                'Fourth Score': [np.nan, np.nan, np.nan, 65]}
        df = pd.DataFrame(dict)

        df.dropna(how='all')
    ```
3. `Dropping Columns with At Least One Null Value`
    - To remove columns that contain at least one missing value we use dropna(axis=1).
    ```
        dict = {'First Score': [100, np.nan, np.nan, 95],
                'Second Score': [30, np.nan, 45, 56],
                'Third Score': [52, np.nan, 80, 98],
                'Fourth Score': [60, 67, 68, 65]}
        df = pd.DataFrame(dict)

        df.dropna(axis=1)
    ```
4. `Dropping Rows with Missing Values in CSV Files`
    - When working with CSV files, we can drop rows with missing values using dropna().
    ```
        import pandas as pd
        d = pd.read_csv("/content/employees.csv")

        nd = d.dropna(axis=0, how='any')

        print("Old data frame length:", len(d))
        print("New data frame length:", len(nd))
        print("Rows with at least one missing value:", (len(d) - len(nd)))
    ```
### 18. What is the difference between loc and iloc in Pandas?
- `loc:` It is label-based i.e you access rows and columns using their labels (row and column names).
    ```
        df.loc[row_labels, column_labels]
    ```
- `iloc:` It is integer-position based and here you access rows and columns using their numeric index positions (row and column numbers).
    ```
        df.iloc[row_positions, column_positions]
    ```
### 19. What is the Significance of Describe function in Pandas?
- In pandas, the describe() function is used to generate summary statistics of a dataset. It helps you quickly understand the distribution, central tendency, and spread of your data.
- When applied to a DataFrame or Series, it automatically calculates:
    - Count – Number of non-null values
    - Mean – Average value
    - Std – Standard deviation (spread of data)
    - Min – Minimum value
    - 25% – First quartile (Q1)
    - 50% – Median (Q2)
    - 75% – Third quartile (Q3)
    - Max – Maximum value
### 20. What is groupby() in Pandas and how is it used?
- The groupby() function in Pandas is used to split the data into groups based on one or more columns, then apply an operation (like aggregation, transformation or filtering) on each group separately.
- Syntax : `df.groupby(by_column)`

### 21. What is Data Aggregation in Pandas?
### 22. What is Time Series in Pandas?
### 23. How to convert a String to Datetime in Pandas?
### 24. What is Time Delta in Pandas?
### 25. What is Multi-Indexing in Pandas?