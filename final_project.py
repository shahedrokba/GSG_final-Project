import project as p
students = []
courses = []
def add_std():
    name = input("Enter Student Name :")
    level = input("Enter Student Class(A-B-C):")
    students.append(p.Student(name,level))
    print("Student Saved Successfully")

def display_all_students():
    if len(students):
        for student in students:
            student.display_std_details()
    else:
        print("no enrolled students")



def remove_student():
    id = int(input("Enter the student id to remove :"))
    for student in students:
        if student.std_id == id:
            students.remove(student)
            print("removed successfully")
        else:
            print("the student is not exist")
def edit_student():
    id = int(input("Enter the student id to edit :"))
    for student in students:
        if student.std_id == id:
            new_name = input("Enter the name :")
            new_level = input("Enter the level (A-B-C) :")
            student.std_name = new_name
            student.std_level = new_level
        else:
            print("the student is not exist")
def create_course():
    c_name = input("Enter the course name :")
    c_level = input("Enter the course level (A-B-C) :")
    courses.append(p.Course(c_name,c_level))

def add_course_to_student():
    id = int(input("Enter the student id :"))
    for student in students:
        if student.std_id == id:
            c_no = int(input("Enter the course id :"))
            for course in courses:
                if course.course_id == c_no:
                    student.add_new_course(course)
                else:
                    print("course is not exist")
        else:
            print("student is not exist")




while(True):

    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display All Students")
    print("5. Create new Course")
    print("6. Add Course to  Student")
    print("7. Exit")
    choice = int(input("Select Choice Please:"))
    match choice:
        case 1:add_std()
        case 2:remove_student()
        case 3:edit_student()
        case 4:display_all_students()
        case 5:create_course()
        case 7:exit()



