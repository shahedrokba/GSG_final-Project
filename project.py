import itertools
class Course:
    id_iter = itertools.count(1)
    def __init__(self,course_name,course_level):
        self.course_id = next(self.id_iter)
        self.course_name = course_name
        self.course_level = course_level

class Student:
    id = 1
    def __init__(self,std_name,std_level):
        self.std_id = Student.id
        Student.id += 1
        self.std_name = std_name
        self.std_level = std_level
        self.courses = []
    def add_new_course(self,course):
       if course.course_level == self.std_level:
           self.courses.append(course)
           print(f"Added successfully {course.course_name} to {self.std_name}")
       else:
           print(f"{course.course_name} is not suitable for {self.std_name}")

    def display_std_details(self):
        print(f"Id : {self.std_id}")
        print(f"name : {self.std_name}")
        print(f"level : {self.std_level}")
        for course in self.courses:
            print(course.course_name)


