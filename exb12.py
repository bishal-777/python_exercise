#using Object,classes and constructor
class Person:

    def __init__(self,str):
        self.name=str

    def talk(self):
        print(f"Hello ,I am {self.name}")


p1=Person('Bishal')
p2=Person('Ram')
p1.talk()
p2.talk()   