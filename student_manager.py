class StudentManager:
    def __init__(self):
        self.students_info = {}
        

    
    def add_student(self,student):
        if student.student_id in self.students_info:
            print(f"Student Id: {student.student_id} already exist in our system!!!")
        else:
            self.students_info[student.student_id] = student
            print("<< Student Added succefully >>")

