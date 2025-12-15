class students:
    def __init__(self,name,id,dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_name(self):
        return self.__name 
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__id 
    def set_id(self,id):
        self.__id = id 
    def get_dob(self):
        return self.__dob
    def set_dob(self,dob):
        self.__dob = dob

    def input(self,name,id,dob):
        self.set_name(name)
        self.set_id(id)
        self.set_dob(dob)
    def list(self):
        print("Student name{} Id{} DoB{}".format(self.get_name(),self.get_id(),self.get_dob()))
class courses:
    def __init__(self,id,name):
        self.__name = name
        self.__id = id
    def get_name(self):
        return self.__name 
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__id 
    def set_id(self,id):
        self.__id = id

    def input(self,id,name):
        self.set_name(name)
        self.set_id(id)
    def list(self):
        print("course id {} course name{}" .format(self.get_id(),self.get_name()))
class marks:
    def __init__(self,course_id,student_id,mark):
        self.__course_id = course_id
        self.__student_id   = student_id
        self.__mark = mark
    def get_course_id(self):
        return self.__course_id 
    def set_course_id(self,course_id):
        self.__course_id = course_id 
    def get_student_id(self):
        return self.__student_id 
    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_mark(self):
        return self.__mark 
    def set_mark(self,mark):
        self.__mark = mark
    
    def input(self,course_id,student_id,mark):
        self.set_course_id(course_id)
        self.set_student_id(student_id) 
        self.set_mark(mark) 
    def list(self):
        print("Course_id {} , Student_id{}, Mark{}",format(self.get_course_id,self.get_student_id, self.get_mark))

def main():
    number_student = int(input("enter number of student"))
    students_list =[]
    for i in range(number_student):
        id = input(f"enter id of student {i+1}:")
        name = input(f"enter name of student {i+1}:")
        dob = input (f"enter dateofbirthday of student {i+1}: ")
        student = students(name,id,dob)
        student.input(name,id,dob)
        students_list.append(student)

    number_course = int(input("enter number of course"))
    courses_list =[]
    for i in range(number_course):
        id = input(f"enter id of course {i+1}")
        name = input(f"enter name of course {i+1}")
        course = courses(id,name)
        course.input(id,name)
        courses_list.append(course)

    number_marks = int(input("Enter number of marks to input: "))
    mark_list =[]
    for i in range(number_marks):
        course_id = input(f"enter course id{i+1}")
        student_id = input(f"enter student id{i+1}")
        mark_value = float(input(f"enter mark of student {i+1} in course {i+1}"))
        mark = marks (course_id,student_id,mark_value)
        mark.input(course_id,student_id,mark_value)
        mark_list.append(mark)
if __name__ == "__main__":
    main()
