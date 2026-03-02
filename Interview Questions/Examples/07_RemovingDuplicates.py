import pandas as pd

data = {
            "Name": ["Alice", "Bob", "Alice", "David"],
            "Age": [25, 30, 25, 40],
            "City": ["NY", "LA", "NY", "Chicago"]
        }

df = pd.DataFrame(data)

# check dataframe is duplicated
print(df.duplicated()) # returns a boolean Series indicating duplicate rows

# Method 1: Remove duplicates using drop_duplicates
unique_df =  df.drop_duplicates() # removes duplicate rows, keeping the first occurrence by default()
print("DataFrame with duplicates removed:\n", unique_df)

# Method 2: Remove duplicates based on specific columns
unique_name_df = df.drop_duplicates(subset=['Name']) # removes duplicates based on the 'Name' column
print("\nDataFrame with duplicates removed based on 'Name':\n", unique_name_df)

# Method 3: Keep the last occurrence of duplicates
unique_last_df = df.drop_duplicates(keep='last') # keeps the last occurrence of duplicates
print("\nDataFrame with duplicates removed, keeping the last occurrence:\n", unique_last_df)

# Method 4: Remove all duplicates (keep=False)
unique_none_df = df.drop_duplicates(keep=False) # removes all duplicates, keeping none of the occurrences
print("\nDataFrame with all duplicates removed (keep=False):\n", unique_none_df)

# Method 5: Remove duplicates in-place
df.drop_duplicates(inplace=True) # modifies the original DataFrame to remove duplicates
print("\nOriginal DataFrame after removing duplicates in-place:\n", df)