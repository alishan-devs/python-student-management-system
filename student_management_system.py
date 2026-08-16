students = {}
# Main menu of the Student Management System
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice (1 to 6) :")

    # Add a new student
    if (choice == "1"):
        while True:
            name = input("Enter student name :").title()
            if (name in students):
                print("Student already exists.")
                continue
            if (name == ""):
                print("Name cannot be empty.")
                continue
            else:
                break
        while True:
            marks = input("Enter student marks :")
            if (marks == ""):
                print("Marks cannot be empty.")
                continue
            marks = int(marks)
            # Validate student marks between 0 and 100
            if (marks < 0 or marks > 100):
                print("Please enter valid marks between 0 to 100")
                continue
            break
        students[name] = marks
        print("Student add successfully.")

    # View all students
    elif (choice == "2"):
        if not students:
            print("No Student found.")
        else:
            print("----- Student List -----")
            count = 1
            for name in students:
                print(f"{count}. Name : {name} | Marks : {students[name]}")
                count += 1

    # Search for a student by name
    elif (choice == "3"):
        search_name= input("Enter student name to search :").title()
        if (search_name in students):
             print(f"{search_name} got {students[search_name]} marks.")
        else:
            print("Student not found.")

    # Update student marks
    elif (choice == "4"):
        update_name = input("Enter student name to update :").title()
        if (update_name in students):
            while True:
                new_marks = input("Enter new marks :")
                if (new_marks == ""):
                    print("Marks cannot be empty.")
                    continue
                new_marks= int(new_marks)
                if (new_marks < 0 or new_marks > 100):
                    print("Please enter valid marks b/w 0 to 100.")
                    continue
                break
            students[update_name] = new_marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    # Delete a student
    elif (choice == "5"):
        delete_name = input("Enter name to delete student :").title()
        if delete_name in students: 
            del students[delete_name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    # Exit the program
    elif (choice == "6"):
        print("Thank you for using Student Management System.")
        break
    
    else:
        print("Invalid choice Please enter a number between 1 to 6.")
