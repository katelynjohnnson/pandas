import pandas as pd

# we have a dictionary that we are bringing
# in as a dataframe
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
# a dataframe can have custom indexes for rows and columns
# each column in a dataframe is a series

# automatically translates into a df
# how to make into a dataframe:
# keys = columns and values = rows
grades = pd.DataFrame(grades_dict)

# names the rows
grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

# this shows Eva only and is only one-dimensional
print(grades['Eva'])
# or
print(grades.Sam)

# gives all of the test scores for test one//returns a series
# loc and iloc for columns
print(grades.loc['Test1'])

# .iloc for an integer so use number index instead of name
print(grades.iloc[1])

# grab test1 through tes3 w loc method...shows all
print(grades.loc['Test1':'Test3'])

# when doing the custom index method, the upper bound is included (loc)
# integer base (iloc), the upper bound is not included
# shows only 0 and 1...this is for consecutive
print(grades.iloc[0:2])

# nonconsecutive:
# when using a comma, you must have a second set
# if you dont, it uses it as x (row) and y (column) values to find a certain value to return
print(grades.loc[['Test1', 'Test3']])
# or
print(grades.iloc[[0, 2]])

# do this because eva and katie aren't next to each other in grades
print(grades.loc['Test1':'Test2', ['Eva', 'Katie']])
# or
print(grades.iloc[0:2, [1, 3]])


# who made a 90 or above
grades90 = grades[grades >= 90]
# shows NaN = not a number...aka didn't pass the test
print(grades90)
# limits so it doesn't show A grades
gradesB = grades[(grades >= 80) & (grades < 90)]
print(gradesB)

# grades A or B
gradesAorB = grades[(grades >= 90) | (grades >= 80)]
print(gradesAorB)

# shows the test 2 grade for eva
print(grades.at['Test2', 'Eva'])
# or
print(grades.iat[1, 1])

# to change a value
# print(grades.at['Test2','Eva']) = 100

# changes number of decimals
pd.set_option('precision', 2)
print(grades.describe())

# transpose shows things by rows (test) instead of columns (names)
print(grades.T.describe())

# sorting with our columns and rows
# sort by the descending index (test3, then 2, then 1):
print(grades.sort_index(ascending=False))
# this sorts by the names of the students
print(grades.T.sort_index(ascending=False))

# or by the columns
# this switches bob and wally
print(grades.sort_index(axis=1))

# sorts by grades rather than test/name
# sorts by test one highest to lowest
# axis = 1 means by columns
print(grades.sort_values(by='Test1', axis=1, ascending=False))

# transposing it: remove axis 1 since it is already by column when transposing
# does it by names as y and test is x instead
print(grades.T.sort_values(by='Test1', ascending=False))

# remove tests 2 and 3 to only show test 1
print(grades.loc['Test1'].sort_values(ascending=False))
