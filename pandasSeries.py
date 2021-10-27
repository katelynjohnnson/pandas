import pandas as pd

# the pd.series creates a series in panda
# the series will be one-dimensional
grades = pd.Series([87, 100, 94])

# dtype = int64 means whole numbers
# dtype = float64 means decimals
# print(grades)

grades2 = pd.Series(98.6, range(3))

# print(grades2)

# print(grades[0])

# gives count, min, max, etx.
# print(grades.describe())

grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])

# or:

# make a pandas series directly from a dictionary
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

# DataFrame = two-dimensional
# every column in a DataFrame is a series
# DataSeries = one-dimensional

print(grades)

print(grades['Eva'])
# or
print(grades.Wally)

print(grades.dtype)

# prints a list of all of the values
print(grades.values)


# create an array of strings
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

print(hardware)

# calling string methods applies ot each element
# this shows which ones contain the letter a...returns as boolean
print(hardware.str.contains('a'))

# returns the values in upper case
print(hardware.str.upper())
