from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        students.append(Student(sid, name, dob))
    return students

def input_courses():
    courses = []
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))
    return courses

def input_marks():
    marks = []
    n = int(input("Enter number of marks: "))
    for _ in range(n):
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        mark = float(input("Mark: "))
        marks.append(Mark(sid, cid, mark))
    return marks

f = open("students.txt", "w", encoding="utf-8")
for s in students:
f.write(f"{s.sid},{s.name},{s.dob}\n")
f.close()

f = open("courses.txt", "w", encoding="utf-8")
for c in courses:
f.write(f"{c.cid},{c.name},{c.credit}\n")

f.close()
f = open("marks.txt", "w", encoding="utf-8")
for m in marks:
f.write(f"{m.student_id},{m.course_id},{m.mark}\n")
f.close()








