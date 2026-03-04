import pandas as pd

startDate = pd.to_datetime("2024-01-01")
endDate = pd.to_datetime("2024-01-10")

timeDelta = endDate - startDate

print("\nThe time delta between the start date and end date is: ", end="\n")
print(timeDelta, end="\n")

# print time delta object in seconds
td = pd.Timedelta(days=1, hours=2, minutes=30)
print("\nThe time delta object in seconds is: ", end="\n")
print(td.total_seconds(), end="\n")

# print time delta object
td1 = pd.Timedelta("3 days 2 hours 52 minutes 15 seconds")
print("\nThe time delta object: ", end="\n")
print(td1, end="\n")

# Print time delta object in a specific format
td2 = pd.Timedelta(weeks = 5, days = 4, hours = 9, minutes = 43, seconds = 34)
print("\nThe time delta object in a specific format: ", end="\n")
print(td2, end="\n")

td3 = pd.Timedelta(4, unit = 'm')
print("\nThe time delta object in minutes: ", end="\n")
print(td3, end="\n")