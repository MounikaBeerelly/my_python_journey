## Note:

1. Every grouping operation in Pandas will involve one OR more number of steps
    1. **Splitting**
        - Splitting is the process where the data is split into the identifies groups, by the applied condition OR conditions on the datasets.
    2. **Applying**
        - Applying is the process where the developer will apply a function to the each identified group independently.
    3. **Combining**
        - Combining is the process where the developer will apply the logic to combine the different datasets after applying the `groupby` and there by collecting the final results into a data structure.

### Points to note when splitting the data into groups
1. Splitting is the process where the data is split inot the identified groups, by the applied condition OR conditions on the datasets.
2. To split the data in the dataset, Pandas provides the `groupby()~ function, where this function has the ability to split the data into groups based on the defined criteria by the developer.
3. Pandas objects can split the data on any of their axes, hence the multiple ways to split the data
    1. pandasObject.groupby(key)
    2. pandasObject.groupby(key,axis = 1)
    3. pandasObject.groupby([key01, key02, ...])
