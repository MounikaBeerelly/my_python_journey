import pandas as pd
import numpy  as np

# Create DataFrames
df1 = pd.DataFrame({
    'Name' : ['Scott', 'Blob'],
    'Age' : [30, 32]
})
df2 = pd.DataFrame({
    'Name' : ['Jones', 'Smith', 'Alice'],
    'Age' : [28, 41, 36]
})

""" Concat method for Merging Dataframes """

# Method 1: Using concat method
merge_df = pd.concat([df1, df2])
print(merge_df)

# Method 2: reset the indexes
merge_df = pd.concat([df1, df2], ignore_index = True)
print(merge_df)

# Method 3: Stacking horizontally
df3 = pd.DataFrame({"City" : ["NJ", "CA"], "Country": ["USA", "USA"]})
merge_df = pd.concat([df1, df3], axis = 1)
print(merge_df)

""" Merge method for Combining Dataframes """