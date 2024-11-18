import math

print("hello world")
print("My first program written in python")
#Basically like a rough copy below
age=20 
name="Bishal"
is_male=True
print(age)
name=input("Enter your name ")
print("hello "+name)
temp=f'''{name}'s age is {age}'''
print(temp)
print(temp.upper())
print(temp.replace("20","25"))
temp2=math.factorial(age)
temp3=f"Factorial of {age} is {temp2}"
print(temp3)
is_hot=False
is_cold=True

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a mild day")