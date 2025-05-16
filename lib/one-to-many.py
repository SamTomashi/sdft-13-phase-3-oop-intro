class TM:
    def __init__(self, name):
        self.name = name
        self.students = [] # one-to-many

    def add_students(self, newStudents):
        self.students.extend(newStudents) # assigns a student to a TM
        for student in newStudents:
            student.tm = self # assigns a TM to a student and 

class Student:
    def __init__(self, name):
        self.name = name
        self.tm = None

chloe = Student("Chloe")
brandon = Student("Brandon")

anita = TM("Anita")

anita.add_students([chloe, brandon])

for student in anita.students:
    print(student.name)
