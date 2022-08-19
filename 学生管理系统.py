class Student(object):
    def __init__(self):
        self.name = input().strip()
        self.student_id = input().strip()
        self.grade = input().strip()
        self.level = list(input().strip())
        self.times = len(self.level)
    def __str__(self) :
        return f"{self.name}'s student number is {self.student_id}, and his grade is {self.grade}. He submitted {self.times} assignments, each with a grade of {' '.join(self.level)}"

stu = Student()
print(stu)