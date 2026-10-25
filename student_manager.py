class StudentManager:
    def __init__(self):
        self.students_info = {}
        

    
    def add_student(self,student):
        if student.student_id in self.students_info:
            print(f"Student Id: {student.student_id} already exist in our system!!!")
        else:
            self.students_info[student.student_id] = student
            print("<< Student Added succefully >>")

    def search_student(self,student_id):
        if student_id in self.students_info:
            return self.students_info[student_id]
        else:
            print("Student not found")
            return None