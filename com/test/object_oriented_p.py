class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades)/len(self.grades)


student = Student("Bob", (54, 45, 12, 79))
print(student.average_grade())
