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

    def update_student(self,student_id):
        try:
            update_std = self.students_info[student_id]
            update_std.name = input("Student Name: ")
            update_std.age = int(input("Studnet Age: "))
            update_std.course = input("Studnet Course: ")
            self.students_info[student_id] = update_std
        except ValueError:
            print("Enter valid Information")

    def delete_student(self,student_id):
        student = self.search_student(student_id)
        if student is not None:
            del self.students_info[student_id]
            print("student deleted succefully")
        

    def display_all_students(self):
        if not self.students_info:
            print("Database empty!!!")
        else:
            for i in self.students_info:
                student = self.students_info[i]
                student.display_details()
