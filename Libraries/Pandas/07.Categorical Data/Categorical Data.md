### What is meant by Categorical Data in Pandas?
1. When extracting the data from real-time sources, which includes the text columns, there is always a chance for repetitive data to be part of the column.
2. Repetititve data is a general a `one-to-many` cardinality of data, and as per the requirement of the data science it is essential in categorical analysis.
    - **Illustrative Examples**:
        - Gender of human beings
        - Country names or country codes
        - any data representing to the specific code of the business.
3. Categorical variables willt ake only a limited and fixed number of possibel values as per the business.
4. Categorical is a general fixed length, and also by circumstantial requirement it may demand a specific order.
5. Categorical data should not OR cannot perform any kind of numerical operations.
6. Pandas provides a categorical datatype to identify the categorical data.

### What are the circumstances under which we use categorical datatype in Pandas?
1. Any Column or Series which contains `String` data with a very few different values, By converting the string variable into the Categorical datatype variable we can definitey save the memory.
2. There are cases where the lexical order of the variable is not same as the logical order of its existence for this data, which makes certain aggregations much faster.
3. When we are operating with different Python Libraries, to make other library to understand that the data we are operating is Categorical