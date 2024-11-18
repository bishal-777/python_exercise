name=input("Enter your name:")
temp=len(name)
if temp<3:
    print("Name must be at least three characters long")
elif temp>50:
    print("Name must not be more than 50 characters long")
else:
    print("You have entered a valid name")
    