import validation
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
            std_info = self.students_info[student_id]     
            return std_info
        else:
            return None

    def update_student(self,student_id):
        student = self.search_student(student_id)
        if student is not None:
            
            update_std = self.students_info[student_id]
            while True:
                name = input("Student Name: ")
                result = validation.string_validation(name)
                if result is not None:
                    update_std.name = result
                    break
                else:
                    print("Invalid Name!!!!!!!!")

            while True:
                age = input("Enter Student Age:")
                result = validation.age_validation(age)
                if result is not None:
                    update_std.age = result
                    break
                else:
                    print("Invalid Age !!!")

            while True:
                course = input("Student Course: ")
                result = validation.string_validation(course)
                if result is not None:
                    update_std.course = result
                    break
                else:
                    print("Invalid Name!!!!!!!!")
                    
            self.students_info[student_id] = update_std
            return True
        else:
            return False


    def delete_student(self,student_id):
        student = self.search_student(student_id)
        if student is not None:
            del self.students_info[student_id]
            return True
        else:
            return False
        

    def display_all_students(self):
        if not self.students_info:
            print("Database empty!!!")
        else:
            for i in self.students_info:
                student = self.students_info[i]
                student.display_details()
