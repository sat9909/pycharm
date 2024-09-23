# A string is essentially a sequence of characters also called an array.
# Thus we can access the elements of this array.


name="satyam"
print("I am "+name)

print('He said, "I want to eat an apple".')
#single quote and double quote fundas

# multiline strings
multiline='''whatever I write here and however in single line or
multiple lines 
I will get no errors, I can even "add" these 'to' the code and good to go'''

print(multiline)

apple='''go beyond
and achieve it all'''

# how to use indexing in strings
print(name[0]) #first character
print(name[1]) #second char
print(name[2]) #so on
print(name[3])
print(name[4])
print(name[5])
# print(name[7])  this is an index error cause no character in 6th position


# Looping through the string
# We can loop through strings using a for loop like this:
print("Using for loop")
for character in name:
    print(character)

for units in apple:
    print(units)
