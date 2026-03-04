import pandas as pd
from datetime import datetime

inDateTime = pd.to_datetime('8/11/2025')

print("\nThe given date in string format 8/11/2025 represented as Date and Time is :", inDateTime, end="\n")


empDataFrame = pd.read_csv(r"C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
empDataFrame["HIREDATE"] = pd.to_datetime(empDataFrame["HIREDATE"], format = '%d-%b-%y')
print("\nThe data is loaded successfully, redirecting the data to the console...", end = "\n")
print("\n", empDataFrame, end="\n")

empDataFrame["HIRETIME"] = pd.to_datetime(empDataFrame["HIREDATE"], format = '%H-%M-%S')

empDataFrame['HIREYEAR'] = empDataFrame['HIREDATE'].dt.year
empDataFrame['HIREMONTH'] = empDataFrame['HIREDATE'].dt.month
empDataFrame['HIREDAY'] = empDataFrame['HIREDATE'].dt.day
empDataFrame['HIREHOUR'] = empDataFrame['HIRETIME'].dt.hour
empDataFrame['HIREMINUTE'] = empDataFrame['HIRETIME'].dt.minute
empDataFrame['HIRESECOND'] = empDataFrame['HIRETIME'].dt.second

print("\n", empDataFrame, end="\n")

# Next day for the given date
currentDateTime = datetime.now()
print("\nThe current date and time captured is : ", currentDateTime)
print("\nPresenting the Date for Tomorrow : ", currentDateTime + pd.to_timedelta(1, unit = 'D'))
print("\nPresenting the Date for next Month : ", currentDateTime + pd.DateOffset(months = 1))
print("\nPresenting the Date for next year : ", currentDateTime + pd.DateOffset(years = 1))

empDataFrame01 = pd.read_csv(r"C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
empDataFrame01["HIREDATE"] = pd.to_datetime(empDataFrame01["HIREDATE"], format = '%d-%b-%y')

# Filter the data for the employees hired in the year 1981
print("\nThe data for the employees hired in the year 1981 is : ", end="\n")
print("\n", empDataFrame01[empDataFrame01["HIREDATE"].dt.year == 1981], end="\n")

# Filter the data for the employees hired in the month of September
print("\nThe data for the employees hired in the month of September is : ", end="\n")
print("\n", empDataFrame01[empDataFrame01["HIREDATE"].dt.month == 9], end="\n")

# Filter the data for the employees hired on the 3rd day of any month
print("\nThe data for the employees hired on the 3rd day of any month is : ", end="\n")
print("\n", empDataFrame01[empDataFrame01["HIREDATE"].dt.day == 3], end="\n")

# Filter the data for the employees hired in the year 1981 and month of December
print("\nThe data for the employees hired in the year 1981 and month of December is : ", end="\n")
print("\n", empDataFrame01[(empDataFrame01["HIREDATE"].dt.year == 1981) & (empDataFrame01["HIREDATE"].dt.month == 12)], end="\n")

# Filter the data from 1981 september to 1981 december
print("\nThe data for the employees hired from 1981 September to 1981 December is : ", end="\n")
print("\n", empDataFrame01[(empDataFrame01["HIREDATE"] >= '1981-09-01') & (empDataFrame01["HIREDATE"] <= '1981-12-31')], end="\n")