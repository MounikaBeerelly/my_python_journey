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
- **Real-World Use Cases** - Pandas is widely used in:
    - Data cleaning & preprocessing
    - Exploratory Data Analysis (EDA)
    - Financial analysis
    - Machine learning pipelines
    - Log analysis
    - Business intelligence dashboards
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
    - The Panadas dataframe petentially manages Heterogeneous tabular data with labelled axes represented as Rows and Columns.
    - Pandas dataframe consists of three principal components
        - Data
        - Rows
        - Columns
### 3. What are the Different Ways to Create a Series?
- In Pandas, a series can be created in many ways. They are as follows:
1. `Creating a Series from a List`
    - We can create a series using a Python list and pass it to the Series() constructor.
    ```
        import pandas as pd

        s = pd.Series([10, 20, 30])
        print(s)
    ```
    - Pandas automatically assigns index 0, 1, 2
2. `From List with Custom Index`
    - Create a Series using Python List and pass the custom indexes
    ```
        s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    ```
3. `Creating a Series from Dictionary` :
    - Create a Series using Python dictionary and pass it to the Series constructor. The keys of the dictionary are become indexes and values becomes data.
    ```
        import pandas as pd

        dict = {'Geeks': 10,'for': 20, 'geeks': 30}

        print(pd.Series(dict))
    ```
4. `From a Scalar Value` :
    - Creates Series with repeated value.
    ```
        s = pd.Series(5, index=["a", "b", "c"])
    ```
5. `From NumPy Array`
    ```
        import numpy as np

        arr = np.array([1,2,3])
        s = pd.Series(arr)
    ```
    - Fast because uses NumPy internally
6. `From Another Series (Copy)`
    - Useful when modifying without affecting original
    ```
        s1 = pd.Series([1,2,3])
        s2 = pd.Series(s1)
    ```
7. `From Range / Sequence`
    ```
        s = pd.Series(range(5))
    ```
8. `Creating a Series using NumPy Functions` :
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
1. `Creating a DataFrame using a List`
    - Pass the list to the DataFrame() constructor.
    ```
        import pandas as pd

        lst = ['Geeks', 'For', 'Geeks', 'is',
        'portal', 'for', 'Geeks']

        print(pd.DataFrame(lst))
    ```
2. `Creating a DataFrame using a Dictionary` :
    - Pass the dictionary to the DataFrame() constructor.
    - The Keys of the dictionary will be the column names and the values of the dictionary are the data of the DataFrame.
    ```
        import pandas as pd

        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}

        print(pd.DataFrame(data))
    ```
3. `Creating a DataFrame using a List of Dictionaries`
    - Pass the list of dictionaries to the Dataframe constructor.
    - Each dictionary represents a row.
    ```
        data = [
            {"name": "A", "age": 25},
            {"name": "B", "age": 30}
        ]

        df = pd.DataFrame(data)
    ```
4. `Creating a DataFrame from Pandas Series`
    ```
        s1 = pd.Series([1,2,3])
        s2 = pd.Series([4,5,6])

        df = pd.DataFrame({"A": s1, "B": s2})
    ```
5. `From CSV File`
    ```
        df = pd.read_csv("file.csv")
    ```
6. `From Excel File`
    ```
        df = pd.read_excel("file.xlsx")
    ```
7. `From JSON`
    ```
        df = pd.read_json("file.json")
    ```
8. `From SQL Database`
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
