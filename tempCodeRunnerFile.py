        case 2:
            print("<<-- Searching Student -->>")

            while True:
                student_id = input("Enter Student Id: ")
                result = validation.integer_validation(student_id)
                if result is not None:                 
                    search_result = manager.search_student(result)
                    if search_result is not None:
                        search_result.display_details()
                        break
                    
                else:
                    print("Invalid Id!!!!!!")

