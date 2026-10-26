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
                student_id = input("Student id: ").strip()
                result = validation.integer_validation(student_id)
                if result is not None:
                    student_id = result
                    break
                else:
                    print("Enter valid Id!!!!!")

            while True:
                name = input("Student Name: ").strip()
                if "" == name:
                    print("Name is empty !!!!!")
                else:
                    break

            while True:
                try:
                    age = int(input("Student Age: "))
                    if  age >= 3 and age <= 120 :
                        break
                    else:
                        print("Valid age range is 3-120 !!!")
                except ValueError:
                    print("Please Enter Valid Integer !!!")

            while True:
                course = input("Student Course: ").strip()
                if "" == course:
                    print("Course is empty !!!!!")
                else:
                    break

        case 2:
            print("<<-- Searching Student -->>")
            try:
                student_id = int(input("Enter Student Id: "))
                if student_id <= 0:
                    print("Enter Valid Student id !!!")
                    continue    
                else:
                    std_info = manager.search_student(student_id)

                if std_info is not None:
                    std_info.display_details()

            except ValueError:
                print("Enter Valid Student id !!!")
                    
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

            