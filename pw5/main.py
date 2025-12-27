import numpy as np

from input import input_students, input_courses, input_marks
from output import print_students

def calculate_gpa(student_id, courses, marks):
    mark_list = []
    credit_list = []

    for m in marks:
        if m.student_id == student_id:
            for c in courses:
                if c.cid == m.course_id:
                    mark_list.append(m.mark)
                    credit_list.append(c.credit)

    if not mark_list:
        return 0.0

    marks_np = np.array(mark_list)
    credits_np = np.array(credit_list)

    return round(np.sum(marks_np * credits_np) / np.sum(credits_np), 2)

def main():
    students = input_students()
    courses = input_courses()
    marks = input_marks()

    for s in students:
        s.gpa = calculate_gpa(s.sid, courses, marks)

    students.sort(key=lambda x: x.gpa, reverse=True)

    print_students(students)

if __name__ == "__main__":
    main()
