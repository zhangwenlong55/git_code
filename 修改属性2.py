class Employee(object):
    def __init__(self):
        self.name = input().strip()
        self.salary = int(input())
    def printclass(self):
        print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")
    

e = Employee()
print(hasattr(Employee,"age"))  
x = int(input())
setattr(Employee,"age",x)
e.printclass()