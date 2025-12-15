import math
import numpy as np

class Student:
    def __init__(self, name, sid, dob):
        self.name = name
        self.sid = sid
        self.dob = dob
        self.gpa = 0.0

class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit

class Mark:
    def __init__(self, course_id, student_id, mark):
        # round DOWN to 1 decimal
        self.course_id = course_id
        self.student_id = student_id
        self.mark = math.floor(mark * 10) / 10

def calculate_gpa(student_id, courses, marks):
    mark_list = []
    credit_list = []

    for m in marks:
        if m.student_id == student_id:
            for c in courses:
                if c.cid == m.course_id:
                    mark_list.append(m.mark)
                    credit_list.append(c.credit)

    if len(mark_list) == 0:
        return 0.0

    marks_np = np.array(mark_list)
    credits_np = np.array(credit_list)

    gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
    return round(gpa, 2)

def main():
    students = []
    courses = []
    marks = []

    # ---- Students ----
    n = int(input("Enter number of students: "))
    for i in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        students.append(Student(name, sid, dob))

    # ---- Courses ----
    m = int(input("Enter number of courses: "))
    for i in range(m):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))

    # ---- Marks ----
    k = int(input("Enter number of marks: "))
    for i in range(k):
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        mark = float(input("Mark: "))
        marks.append(Mark(cid, sid, mark))

    # ---- Calculate GPA ----
    for s in students:
        s.gpa = calculate_gpa(s.sid, courses, marks)

    # ---- Sort by GPA descending ----
    students.sort(key=lambda x: x.gpa, reverse=True)

    print("\n=== STUDENT GPA LIST (DESCENDING) ===")
    for s in students:
        print(f"ID: {s.sid}, Name: {s.name}, GPA: {s.gpa}")

if __name__ == "__main__":
    main()
