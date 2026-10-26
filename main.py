import student
import student_manager
import validation

print("==== STUDENT MANAGEMENT SYSTEM ====\n")
print("1. Add Student")
print("2. Search Student")
print("3. Update Student")
print("4. Delete Student")
print("5. Display All Student")
print("6. Exit")

manager = student_manager.StudentManager()

while True:
    try:
        user_choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid Input!!!! Please chose valid choice")
        continue
    
    match user_choice:
        case 1:
            print("<<-- Enter information -->>")
            while True:
                student_id = input("Student id: ")
                result = validation.integer_validation(student_id)
                if result is not None:
                    student_id = result
                    break
                else:
                    print("Enter valid Id!!!!!")

            while True:
                name = input("Student Name: ")
                result = validation.string_validation(name)
                if result is not None:
                    name = result
                    break
                else:
                    print("Invalid Name!!!!!!!!")

            while True:
                age = input("Student Age: ")
                result = validation.age_validation(age)
                if result is not None:
                    age = result
                    break
                else:
                    print("Valid range of age is 3-120")

            while True:
                course = input("Student Course: ")
                result = validation.string_validation(course)
                if result is not None:
                    course = result
                    break
                else:
                    print("Invalid course Name!!!!")   
            std = student.Student(student_id,name,age,course)  
            manager.add_student(std)                

        case 2:
            print("<<-- Searching Student -->>")

            while True:
                student_id = input("Enter Student Id: ")
                result = validation.integer_validation(student_id)
                if result is not None:
                    manager.search_student(result)
                    break
                else:
                    print("Invalid Id!!!!!!")

        case 3:
            print("<<= Updating Student Data =>>")
            try:
                student_id = int(input("Enter Student Id: "))
                if student_id <= 0: 
                    print("Enter Valid Student id !!!")
                    continue
                else:
                    std_info = manager.update_student(student_id)
                                  
            except ValueError:
                print("Enter Valid Student id !!!")
                                
        case 4:
            print("<<= Deleting Student =>>")
            try:
                student_id = int(input("Student Id: "))
                manager.delete_student(student_id)
            except ValueError:
                print("enter valid Id!!!!")

        case 5:
            print("<<-- All Students List -->>")
            manager.display_all_students()
        case 6:
            print("Exited") 
            break
        case _:
            print("invalid choice!!!!")

            