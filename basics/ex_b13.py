class Triangle:

    def perimeter(self):
        a,b,c=map(int,input("Enter length of all 3 sides of triangle").split())
        p=a+b+c
        print("Perimeter of traingle:{p}")

class Circle:

    def perimeter(self):
        a,b,c=map(int,input("Enter length of all 3 sides of triangle").split())
        p=a+b+c
        print("Perimeter of traingle:{p}")

class Square:

    def perimeter(self):
        a,b,c=map(int,input("Enter length of all 3 sides of triangle").split())
        p=a+b+c
        print("Perimeter of traingle:{p}")



class Area:
    def calc(Triangle):
        choice=int(input("Enter 1 for circle\nEnter 2 for Triangle\nEnter 3 for square"))

        match choice:
            case 1:
               r=int(input("Enter radius of circle:"))

            case 2:
                b,h=map(int,input("Enter base and height of traingle:").split()) 

            case 3:
                l=int(input("Enter length of square:"))

            case _:
                print("Enter a valid option")



        
