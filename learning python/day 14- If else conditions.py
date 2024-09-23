# An if……else statement evaluates like this:
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.\
#
# if the expression evaluates False:
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# Based on this, the conditional statements are further classified into following types:
#
# if
# if-else
# if-else-elif
# nested if-else-elif.

#Examples
#if else statements

price_of_chhoti_advance=10
price_of_badi_advance=15
budget=16652364646456

if (price_of_badi_advance <= budget):
    print("Maje maje bhai")
else:
    print("aaj kam me kaam chalana padega")

#elif statements

num=4
if (num <0):
    print(num,"is negative")
elif (num==0):
    print("Number is zero")
else:
    print(num,'is positive')


#nested if statements

# We can use if, if-else, elif statements inside other if statements as well.

num=int(input("Enter a number:"))
if (num < 0):
    print(num,'is Negative')
elif (num > 0):
    if(num<=10):
        print(num,"is between 1-10")
    elif(num > 10 and num <=20):
        print(num,'is between 11-20')
    else:
        print(num,"is greater than 20")
else:
    print("Number is Zero")


