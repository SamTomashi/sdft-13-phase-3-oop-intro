class Course:
    def __init__(self, title):
        self.title = title
        self.students = []  #many-to-many relationship


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = [] #many-to-many relationship

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)
            print(f"Hi {self.name}, you have successfully enrolled to the {course.title} class")
        else:
            print(f"Sorry {self.name}, you have already enrolled to the {course.title} class")

DS = Course("Data Science")
SD = Course("Software Development")

rose = Student("Rose")
rose.enroll(SD)
rose.enroll(DS)


mazal = Student("Mazal")
mazal.enroll(SD)
mazal.enroll(DS)




# for student in SD.students:
#     print(f"{student.name} has enrolled to the SD class")

# for student in SD.students:
#     print(student.name)




    

