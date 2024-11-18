#Weight converter
weight=int(input("Enter your weight:"))
unit=input("Is your weight in kg or lb?").lower()
if unit=="kg":
    weight=2.2
    print(f"Weight in lb: {weight}")
elif unit=="lb":
    weight/=2.2
    print(f"Weight in kg: {weight}")
else:
    print("Enter a valid unit!")