# strings are immutable but we can alter and modify the strings

st1=("golgappe BADE Achhe")
print(st1)

print(st1.upper()) #for uppercase every letter

print(st1.lower()) #for lowercase every letter

st2="            main hun bhagwan     "
print(st2)
print(st2.strip())  #removes any whitespaces before or after string

st3="main mahan hun !!!"
print(st3)
print(st3.rstrip("!"))   #removes any trailing char (only after the string not before)


st4="I am in Patna"
print(st4)
print(st4.replace("Patna","Kanpur"))  #replace all occurances of a string with another string
st4="I am in Patna Patna"
print(st4.replace("Patna","Kanpur"))

st5="Silver Spoon"
print(st5.split(" "))   #splits the given string at specified instance and return separated string as list items
st5="this is an # automatic # message"
print(st5.split("#"))

st6="this is an awesome poem. OOPS i FOrgot the capitalization"
print(st6.capitalize())

st7="This method centralise the string"
# print(st7.center())   #this throws an error
print(st7.center(100))  #have to give more than len number in the () it will make the str of given len in () by adding space in front
print(st7.center(50,"."))

st8="this contains so many times aaaaaaaaaaaaaaaaaa"
print(st8.count("a"))  #counts how many times given char appears
print(st8.count("contains"))

st9 = "Welcome to HEAVEN !!!"
print(st9.endswith("!!!"))

print(st9.endswith("come", 2,7 ))


#The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1
st10="I am the best of the best"
print(st10.find("the"))

#The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(st10.index("of"))


st11="soletsfindlove20"
print(st11)
print(st11.isalnum())  #tells if strings contains only alphanumeric i.e A-Z, a-z. 0-9
print(st11.isalpha())  #tells about A-Z, a-z
# ,.#!$@'" if any symbol exist it will give an error
st11="so let's find love"
print(st11.isalnum())

print(st11.islower()) #name tells all

print(st11.isprintable()) # tells if all the char are printable or not

st12=("     ")
print(st12.isspace())  #returns true if all char are whitespaces
print(st11.isspace())  #returns true if all char are whitespaces

st13="World is mine"
print(st13.istitle())  #returns true if first char of all letters are capitalised

st13="World Is Mine"
print(st13.istitle())

st14="YYUADDADAD"
print(st14.isupper())  #returns true if all letters are uppercase

st15="My life is beautiful"
print(st15.startswith("My"))  #returns true if string starts with given word

st16="I live a good life. my family is beautiful"
print(st16.swapcase())

st17="I bought a USB hub "
print(st17.title())  #capitalise first letter of each word

