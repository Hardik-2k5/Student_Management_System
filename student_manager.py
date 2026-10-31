import validation
import json

class StudentManager:
    def __init__(self):
        self.students_info = {}
        self.get_json()

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
                    update_std.name[result]
                    break
                else:
                    print("Invalid Name!!!!!!!!")

            while True:
                age = input("Enter Student Age:")
                result = validation.age_validation(age)
                if result is not None:
                    update_std.age[result]
                    break
                else:
                    print("Invalid Age !!!")

            while True:
                course = input("Student Course: ")
                result = validation.string_validation(course)
                if result is not None:
                    update_std.course[result]
                    break
                else:
                    print("Invalid Name!!!!!!!!")
                    
            self.students_info[student_id] = update_std

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

    def get_json(self):
        raw_data = {}
        try:
            with open("Students.json","r") as data:
                raw_data = json.load(data)
            for i in raw_data:
                const_std = const_std(**raw_data[i])
                self.students_info[const_std.student_id] = const_std
                
        except FileNotFoundError:
            with open("Students.json","w") as data:
                json.dump(self.students_info,data,indent=4)

    def store_json(self):
        raw_data = {}
        for i in self.students_info:
            std_obj = self.students_info[i]
            student = std_obj.__dict__
            raw_data[std_obj.student_id] = student
        with open("Students.json","w")as data:
            json.dump(raw_data,data,indent= 4)