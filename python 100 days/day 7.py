#making a calculator


# Arithmetic operators
# Operator	Operator Name	Example
# +	Addition	15+7
# -	Subtraction	15-7
# *	Multiplication	5*7
# **	Exponential	5**3
# /	Division	5/3
# %	Modulus	15%7
# //	Floor Division	15//7

n=float(input("Enter first number:-"))
m=float(input("Enter second number:-"))

ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 =n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)