import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

print(grades)

eva = grades["Eva"]

sam = grades.Sam

# using the loc and iloc methods

test2 = grades.loc["Test2"]

test1 = grades.iloc[0]

# for consecutive rows
# use : for consecutive rows
test1_thru_test3 = grades.loc["Test1":"Test3"]
# use , and list [] for non-consecutive rows
test1_and_test3 = grades.loc[["Test1", "Test3"]]

test1_and_test2 = grades.iloc[0:2]


# view only eva's and katie's grades for test1 and test2

eva_katie_test1_test2 = grades.loc["Test1":"Test2", ["Eva", "Katie"]]

# view only sam's THRU BOB's grades for test1 and test3

sam_thru_bob_test1_test2 = grades.loc[["Test1", "Test3"], "Sam":"Bob"]

# boolean indexing
# select everyone with an A grade
grades_A = grades[grades >= 90]

# create a dataframe for everyone iwth a B grade
grades_B = grades[(grades >= 80) & (grades < 90)]

# everyone wiht an A or B
grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]

pd.set_option("precision", 2)

# by student
print(grades.describe())

# by test
print(grades.T.describe())

# exercise - get average grade of all students on each test
print(grades.T.mean())

# sort rows by theur indices (Test names)
r_sorted_grades_i = grades.sort_index(ascending=False)

# soret coloumns by their coloumn names (student names)
# axis = 1 to sprt by column indicies
# axis = 0 to sort by row
c_sorted_grades_i = grades.sort_index(axis=1)

# in reverse sort order
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)


print()
