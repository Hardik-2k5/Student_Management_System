import student
import student_manager

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
            try:
                student_id = int(input("Student id: "))
                name = input("Student Name: ")
                age = int(input("Student Age: "))
                course = input("Course: ")

                std = student.Student(student_id,name,age,course)
                manager.add_student(std)

            except ValueError:
                print("Enter Valid Information!!!!")
                continue

        case 2:
            print("searching student")
        case 3:
            print("updating student")
        case 4:
            print("deleting student")
        case 5:
            print("all students list")
        case 6:
            print("Exited") 
            break
        case _:
            print("invalid choice!!!!")
           