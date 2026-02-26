## Data Structures supported by Pandas:

- Pandas provides three different data structures for manipulating the data
    - Series
    - DataFrame
    - Panel
- All data structures in Pandas are built on top of `NumPy array`, hence can handle numerical data with absolute speed and fastness.
- All Pandas data structures follow the concept of Higher dimensional data structure is a container of its lower dimensional data structure
    - Data frame is a container of Series
    - Panel is a container of data frame
- Pandas data structures are designed to handle
    - Integer
    - String
    - Float
    - Python Object

### What is Series Data Structure in Pandas?

- Series is a `one-dimensional labelled array` like structure with `homogeneous data`.
- Series can hold any data type
- The axis labels represented in plotting are collectively called as `index`.
- Pandas Series data structure is can be considered like a `column` in an excel sheet
- Series labels need not be unique but they must be a hashable type
- The Pandas Series object supports both `integer and label-based indexing`.
- Pandas Series provides a host of methods for performing operations involving the index.
- The key points to note about series are
    - Can manage homogeneous data
    - The size of the Series is immutable
    - The values of data in Series is mutable

#### Syntax:
    ```
    empnoSeries = pd.Series(df['EMPNO'])
    enameSeries = pd.Series(df['ENAME'])
    ```

### What is DataFrame Data Structure in Pandas?

- DataFrame is a two dimensional array with heterogeneous data.
- The size of the dataframe is mutable.
- The Panadas dataframe petentially manages Heterogeneous tabular data with labelled axes represented as `Rows and Columns`.
- The total data loaded into Pandas dataframe is aligned as a relational table, with `Rows and Columns`.
- Pandas dataframe consists of three principal components
    - Data
    - Rows
    - Columns

- **`When sorting, it is not rearranging the index numbers`**