# Exercise: Python Variables
# 1.Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

#break= 5    # this generates an error as break is a function assigned to perform a specific task thus can't be assigned a variable.

# 2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

birthyear=2002
currentyear=2024
age=currentyear-birthyear
print(age)


# 3. Store your first, middle and last name in three different variables and then print your full name using these variables

fname= "Satyam"
mname= "Kumar"
lname= "Singh"
print(fname,mname,lname)

# Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue

# Invalid names are
_nation=3
# 1record=2         #invalid
record1=4
record_one=5
# record-one= 3          invalid
# record^one=3           invalid
# continue=2             invalid