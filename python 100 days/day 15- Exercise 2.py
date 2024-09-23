import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
print(timestamp1)
timestamp2 = time.strftime('%M')
print(timestamp2)
timestamp3 = time.strftime('%S')
print(timestamp3)
# https://docs.python.org/3/library/time.html#time.strftime

if timestamp1 >= 4 and timestamp1 < 11:
    print("Good Morning Sir")
elif timestamp1 >=11 and timestamp1 < 14:
    print("Good Noon Sir")
elif timestamp1 >=14 and timestamp1 < 16:
    print("Good Afternoon Sir")
elif timestamp1 >=16 and timestamp1 < 20:
    print("Good Evening Sir")
else:
    print ("So ja yarr kitna kaam karwaega")
    
