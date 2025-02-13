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

i=1
while i<=5:
 print(i)
 i+=1
print("-----")

students=['Ram','Shyam','Hari']
for i in students:
    print(i)
for i in range(2,9,2):
    print (i)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix[1][1]=99
print(matrix[1][1])

num=[2,7,4,1,9]
num2=num.copy()
num.append(67)
num.insert(2,76)
num.pop()
num.sort()
print(num)
print(num2)
