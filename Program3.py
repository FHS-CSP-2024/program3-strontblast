## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"My name is {name}, I am {age} years old")
print("\t")
print("my skills are")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print(f"- {skill3} ({level3})")
print("\t")
print(f"I am looking for a job with a salary of {lower}-{upper} dollars per month")


## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")
number = int(x)
number1 = int(y)
result = number + number1
result1 = number - number1
result2 = number * number1
result3 = number / number1
print("\t")
print(f"{x} + {y} = {result}")
print(f"{x} - {y} = {result1}")
print(f"{x} * {y} = {result2}")
print(f"{x} / {y} = {result3}")