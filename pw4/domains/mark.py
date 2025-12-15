import math

class Mark:
    def __init__(self, student_id, course_id, mark):
        # round down to 1 decimal
        self.student_id = student_id
        self.course_id = course_id
        self.mark = math.floor(mark * 10) / 10
