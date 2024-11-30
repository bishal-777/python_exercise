#finds largest number in a list
num=[2,7,4,3,0,2,1,9,6]
largest=num[0]
for i in num: 
    if i>largest:
        largest=i
print(f"Largest number={largest}")