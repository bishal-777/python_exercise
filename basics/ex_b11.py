#calculates roots of equation whic uses expection handling
import math

a,b,c=map(int,input("Enter the value of a,b and c of the quadratic equation:").split())
try:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)

    print(f"x={x1},{x2}")

except ZeroDivisionError:
    print("Enter valid value for 'a'")
