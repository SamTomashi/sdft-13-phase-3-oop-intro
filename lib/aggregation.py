'''
A class has-a relationship with other. But they can both exist indepently
'''

class Course:
    def __init__(self, title):
        self.title = title

    

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, newCourses):
        self.courses.extend(newCourses)


    def show_courses(self):
        for course in self.courses:
            print(f"{self.name} offers {course.title}")

ds = Course("Data Science")
sd = Course("Software Development")


department1 = Department("IT")

department1.add_course([ds, sd])

department1.show_courses()