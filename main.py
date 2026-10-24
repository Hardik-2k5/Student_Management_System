print("==== STUDENT MANAGEMENT SYSTEM ====\n")
print("1. Add Student")
print("2. Search Student")
print("3. Update Student")
print("4. Delete Student")
print("5. Display All Student")
print("6. Exit")

while True:
    try:
        user_choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid Input!!!! Please chose valid choice")
        continue
    
    match user_choice:
        case 1:
            print("adding student")
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
           