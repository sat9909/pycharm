# i=0
# while (i<5):
#     print(i)
#     i=i+1     # if we don't put this value of i remains 0 and only 0 prints for infinite times in the machine
from itertools import count

ink=0   # a name should be defined before every while loop, not like for loop
while (ink<=20):
    ink=int(input("Enter a number:"))
    print(ink)

print("Number is grater than 20")


#decrementing while loop
count= 5
while (count > 0):
  print(count)
  count = count - 1

# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as
# soon as the while loop condition becomes False, the interpreter comes out of the while loop and the
# else statement is executed.

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
