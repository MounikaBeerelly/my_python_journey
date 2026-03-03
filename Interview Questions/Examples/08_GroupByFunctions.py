import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

groupbyDept = empDataFrame.groupby("DEPTNO")
print("The grouped data by department is: \n", groupbyDept.groups, end="\n")

print("\nThe first record of each group is: \n", groupbyDept.first(), end="\n")

# calculate avg salry of each department
avgSal = empDataFrame.groupby("DEPTNO")["SAL"].mean()
print("\nThe average salary of each department is: \n", avgSal, end="\n")

# calculate the sum of salary of each department
sumSal = empDataFrame.groupby("DEPTNO")["SAL"].sum()
print("\nThe sum of salary of each department is: \n", sumSal, end="\n")

# Calculate the count of employees in each department
countEmp = empDataFrame.groupby("DEPTNO")["EMPNO"].count()
print("\nThe count of employees in each department is: \n", countEmp, end="\n")

# Calculate the minimum, maximum and standard deviation of salary in each department
groupData = empDataFrame.groupby("DEPTNO").aggregate({"SAL": ["min", "max", "std"]})
print("\nThe minimum, maximum and standard deviation of salary in each department is: \n", groupData, end="\n")

# Calculate the sum of salary of each department and job
empDeptJobSum= empDataFrame.groupby(["DEPTNO", "JOB"])["SAL"].sum()
print("\nThe sum of employees department and Job wise: ", empDeptJobSum)

# count the number of employees in each department and job
empDeptJobCount = empDataFrame.groupby(["DEPTNO", "JOB"])["EMPNO"].count()
print("\nThe count of employees department and Job wise: ", empDeptJobCount)

# Cumulate the sum of salary
empDeptCumSum = empDataFrame["SAL"].cumsum()
print("\nThe cumulative sum of salary is: \n", empDeptCumSum, end="\n")

# Cumulate the sum of salary department wise
empDeptCumSum = empDataFrame.groupby("DEPTNO")["SAL"].cumsum()
print("\nThe cumulative sum of salary department wise is: \n", empDeptCumSum, end="\n")

# Cumulate the sum of salary department and job wise
empDeptJobCumSum = empDataFrame.groupby(["DEPTNO", "JOB"])["SAL"].cumsum()
print("\nThe cumulative sum of salary department and job wise is: \n", empDeptJobCumSum, end="\n")