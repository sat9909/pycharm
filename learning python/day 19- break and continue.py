# The break statement enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within.

for i in range(3,24):
    print(i)
    if (i==10):  #10 will print too
        break

print("thankyou")


# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in range (3,45):
    if (i==20):
        continue
    print(i)

