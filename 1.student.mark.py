# ===========================================
# Student Mark Management System (No OOP)
# Using: tuples, dicts, lists ONLY
# ===========================================

students = []       # list of dicts: {id, name, dob}
courses = []        # list of dicts: {id, name}
marks = {}          # dict: {course_id: {student_id: mark}}


# ---------------------------------------
# INPUT FUNCTIONS
# ---------------------------------------

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Student DoB (dd/mm/yyyy): ")

        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })
    print("Students added.\n")


def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({
            "id": cid,
            "name": name
        })
        marks[cid] = {}   # prepare mark storage for this course
    print("Courses added.\n")


def input_marks_for_course():
    # list available courses
    print("\nAvailable courses:")
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    cid = input("Enter course ID to input marks: ")

    # find course
    course_ids = [c["id"] for c in courses]
    if cid not in course_ids:
        print("Course not found!\n")
        return

    print("\nEnter marks for students in course:", cid)
    for s in students:
        mark = float(input(f"Mark for {s['name']} ({s['id']}): "))
        marks[cid][s["id"]] = mark

    print("Marks saved.\n")


# ---------------------------------------
# LISTING FUNCTIONS
# ---------------------------------------

def list_courses():
    print("\n===== COURSE LIST =====")
    for c in courses:
        print(f"ID: {c['id']} - Name: {c['name']}")
    print()


def list_students():
    print("\n===== STUDENT LIST =====")
    for s in students:
        print(f"ID: {s['id']} - Name: {s['name']} - DoB: {s['dob']}")
    print()


def show_student_marks_by_course():
    print("\nAvailable courses:")
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    cid = input("Enter course ID: ")

    if cid not in marks:
        print("Course not found!\n")
        return

    print(f"\n===== Marks for course {cid} =====")
    for s in students:
        sid = s["id"]
        if sid in marks[cid]:
            print(f"{s['name']} ({sid}): {marks[cid][sid]}")
        else:
            print(f"{s['name']} ({sid}): No mark")
    print()


# ---------------------------------------
# MAIN MENU
# ---------------------------------------

def main():
    while True:
        print("===== STUDENT MARK SYSTEM =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks_by_course()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
