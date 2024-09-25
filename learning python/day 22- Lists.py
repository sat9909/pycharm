# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.


lst1=[1,2,3,4,5,6]
lst2=["Red","Yellow","Blue"]
print(lst1)
print(lst2)

details=["Vishwa", 29, "AITH", 3.4]
print(details)


# List Index
# Each item/element in a list has its own unique index.
# This index can be used to access any particular item from the list.
# The first item has index [0], second item has index [1], third item has index [2] and so on.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

# Accessing list items
# We can access list items by using its index with the square bracket syntax [].
# For example colors[0] will give "Red", colors[1] will give "Green" and so on...
#
# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items,
# but from the end of the list. The last item has index [-1], second last item has index [-2],
# third last item has index [-3] and so on.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

colors=["Red","types"]
if "Red" in colors:
    print("Red is present")
else:
    print("Red is absent")


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

# Range of Index:
# You can print a range of list items by specifying where you want to start,
# where do you want to end and if you want to skip elements in between the range.
#
# Syntax:
#
# listName[start : end : jumpIndex]
# Note: jump Index is optional. We will see this in later examples.

animals = ["cat",'dog','bat','mouse','pig','horse','donkey', 'goat']
print(animals[2:5])     #using positive index
print(animals[-6:-2])   #using negative index

print(animals[:4])     #prints from 0
print(animals[2:])     #prints from 2 to last
print(animals[::2])    #prints from 0 to last with 2 separation

print(animals[1:7:3])  #prints from 1 to 6 with 3 alternatives


# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
#
# Syntax:
# List = [Expression(item) for item in iterable if Condition]
#
# Expression: It is the item which is being iterated.
#
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
#
# Condition: Condition checks if the item should be added to the new list or not.


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

kilos=["road","opear",'uishsio',"oister"]
perm=[item for item in kilos if "o" in item]
print(perm)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)