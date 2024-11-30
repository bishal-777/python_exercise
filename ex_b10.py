#removes reduntant elements from a list
num=[2,4,7,4,2,9,3,1,9]
num2=[]
for i in num:
   if i not in num2:
      num2.append(i)

print(f"Old list with redundant elements={num}")     
print(f"new list with redundancy eliminated:{num2}")
