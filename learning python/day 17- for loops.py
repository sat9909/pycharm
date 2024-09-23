# Two types of loops for and while
# when we want to execute a group of statements certain amount of times
# for loops can iterate over a sequence of iterable objects in python.
# Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

name= "satyam"
for i in name:
    # print(i)
    print(i, end=".")

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

# we can even find use for loop for a specific number of times

for k in range(5):  # start from 0
    print(k+1)

# for k in range (4,1111):  #range goes to n-1  (1110)
#     print(k)

for fr in range(3,33,5):  #third number gives how much separation we need between numbers
    print (fr)