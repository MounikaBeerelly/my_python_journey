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
# Method 1 : Basic Merge (Inner Join)
dataframe01 = pd.DataFrame({
    'ID' : [1, 2, 3, 4, 5],
    "Name" : ['Scott', 'Blob', 'Jones', 'Smith', 'Alice'],
    "Age" : [30, 32, 28, 41, 36],
    "City" : ["NJ", "CA", "NY", "TX", "FL"]
})

dataframe02 = pd.DataFrame({
    "ID" : [1, 2, 3, 5, 7],
    "Salary" : [70000, 80000, 60000, 75000, 90000],
    "Department" : ["IT", "HR", "Finance", "Marketing", "Sales"]
})

merger_df = pd.merge(dataframe01, dataframe02, on = "ID", how = "inner")
print("\nMerged DataFrame using Inner Join: \n", merger_df)

# Method 2: Outer Join
merger_df = pd.merge(dataframe01, dataframe02, on = "ID", how = "outer")
print("\nMerged DataFrame using Outer Join: \n", merger_df)

# Method 3: Left Join
merger_df = pd.merge(dataframe01, dataframe02, on = "ID", how = "left")
print("\nMerged DataFrame using Left Join: \n", merger_df)

# Method 4: Right Join
merger_df = pd.merge(dataframe01, dataframe02, on = "ID", how = "right")
print("\nMerged DataFrame using Right Join: \n", merger_df)

# Method 5: Merge on different columns
dataframe03 = pd.DataFrame({
    "EmployeeID" : [1, 2, 3, 4, 6],
    "Department" : ["IT", "HR", "Finance", "Marketing", "Sales"]
})
merge_df = pd.merge(dataframe01, dataframe03, left_on = "ID", right_on="EmployeeID")
print("\nMerged DataFrame on different columns: \n", merge_df)

# MEthod 6: Merge on multiple columns
dataframe04 = pd.DataFrame({
    "ID" : [1, 2, 3, 4, 5],
    "City" : ["NJ", "NE", "NY", "TX", "FL"],
    "Country" : ["USA", "USA", "USA", "USA", "USA"]
})
merge_df = pd.merge(dataframe01, dataframe04, on = ["ID", "City"])
print("\nMerged DataFrame on multiple columns: \n", merge_df)

# Method 7 : Merge using indexes
merge_df = pd.merge(dataframe01, dataframe02, left_index = True, right_index = True)
print("\nMerged DataFrame using indexes: \n", merge_df)


""" Merging csv files using merge method"""

# Assuming we have two CSV files: 'employees.csv' and 'Department.csv'
# employees.csv contains columns : EMPNO,ENAME,JOB,MGR,HIREDATE,HIRETIME,SAL,COMM,DEPTNO
# department.csv contains columns : DEPTNO,DNAME,LOC

# Load the CSV files into DataFrames
employees_df = pd.read_csv(r"C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
department_df = pd.read_csv(r"C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

# Method 1: Merge the dataframes using inner join on DEPTNO
merged_df = pd.merge(employees_df, department_df, on = "DEPTNO", how = "inner")
print("\nMerged DataFrame using Inner Join: \n", merged_df)

# Method 2: Merge the dataframes using outer join on DEPTNO
merged_df = pd.merge(employees_df, department_df, on = "DEPTNO", how = "outer")
print("\nMerged DataFrame using Outer Join: \n", merged_df)

# Method 3: Merge the dataframes using Left join on DEPTNO
merged_df = pd.merge(employees_df, department_df, on = "DEPTNO", how = "left")
print("\nMerged DataFrame using Left Join: \n", merged_df)

# Method 2: Merge the dataframes using right join on DEPTNO
merged_df = pd.merge(employees_df, department_df, on = "DEPTNO", how = "right")
print("\nMerged DataFrame using Right Join: \n", merged_df)


""" Merging dataframe using Joins """


# Set the index for both dataframes to DEPTNO
employees_df.set_index("DEPTNO", inplace = True)
department_df.set_index("DEPTNO", inplace = True)

# Method 1: Using Join method for merging dataframes

# Join the dataframes using the join method
joined_df = employees_df.join(department_df, how = "inner")
print("\nJoined DataFrame using Join method: \n", joined_df)

# Method 2: Left Join using Join method

joined_df = employees_df.join(department_df, how = "left")
print("\nJoined DataFrame using Left Join: \n", joined_df)

# Method 3: Right Join using Join method
joined_df = employees_df.join(department_df, how = "right")
print("\nJoined DataFrame using Right Join: \n", joined_df)

# Method 4: Outer Join using Join method
joined_df = employees_df.join(department_df, how = "outer")
print("\nJoined DataFrame using Outer Join: \n", joined_df)

# Show only specific columns after join
print(employees_df)
print(department_df)
joined_df = employees_df.join(department_df, how = "inner", on = "DEPTNO").reset_index()
print("\nJoined DataFrame with specific columns: \n", joined_df[["ENAME",  "DEPTNO", "DNAME"]])