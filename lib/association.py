#Association relationship:

class Student:
    def __init__(self, name):
        self.name = name

class TM:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_students(self, newStudents):
        self.students.extend(newStudents)

    def list_students(self):
        for student in self.students:
            print(f"The technical mentor {self.name} mentors {student.name}")

saint = Student("Saint")
winnie = Student("Winnie")
benjamin = Student("Benjamin")
derick = Student("Derrick")

tomashi = TM("Tomashi")
tomashi.add_students([saint, winnie, benjamin, derick])

tomashi.list_students()