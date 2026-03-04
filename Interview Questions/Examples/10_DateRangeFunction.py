import pandas as pd

datesDataframe = pd.date_range('3/4/2026', periods = 5, freq = 'D')
print("\nThe range of dates generated for every one day starting from 3rd April 2026 are...", end="\n")
print(datesDataframe)

datesDataframe1 = pd.date_range('3/4/2026', periods = 5, freq = 'ME')
print("\nThe range of dates generated for every one month starting from 3rd April 2026 are...", end="\n")
print(datesDataframe1)

datesDataframe2 = pd.date_range(start = '3/4/2026', end = '4/4/2026', periods = 10)
print("\nThe range of dates generated for every one month starting from 3rd April 2026 to 3rd April 2027 are...", end="\n")
print(datesDataframe2)

datesDataframe3 = pd.date_range(start = '3/4/2026', periods = 6, freq = 'h')
print("\nThe range of dates generated for every two months starting from 3rd April 2026 to 3rd April 2027 are...", end="\n")
print(datesDataframe3)

datesDataframe4 = pd.date_range(start = '3/4/2026', end = '3/4/2027', freq = '2ME')
print("\nThe range of dates generated for every two months starting from 3rd April 2026 to 3rd April 2027 are...", end="\n")
print(datesDataframe4)

datesDataframe5 = pd.date_range(start = '3/4/2026', end = '3/10/2026', tz = 'Asia/Kolkata')
print("\nThe range of dates generated for every one day starting from 3rd April 2026 to 3rd April 2027 with timezone as Asia/Kolkata are...", end="\n")
print(datesDataframe5)