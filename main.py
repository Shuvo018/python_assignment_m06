import json
import os
from datetime import datetime
from students import student
from student_details import student_details

JSON_FILE = "student_records.json"

def create_json_file():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as file:
            json.dump([], file, indent=5)
            
def menu():
    print("\n" + "="*8 + " MENU " + "="*8)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    user_input = -1
    try:
        user_input = int(input("Enter your choice: "))
    except Exception as e:
        print("Please enter integer digit. e.g: 1,2,3...")
        return menu()
    
    if user_input < 1 or user_input > 5:
        print("Please enter number from menu 1 to 5")
        return menu()
    
    return user_input



def main():
    # Create JSON file on startup
    create_json_file()
    
    while True:
        choice = menu()
        
        if choice == 1:
            try:
                name = input("Enter student name: ")
                roll = int(input("Enter roll number: "))
                email = input("Enter email: ")
                dept = input("Enter department: ")
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            if not name or not roll or not email or not dept:
                print("All fields are required")
                continue

            std = student(name, roll, email, dept)

            std.add_student(JSON_FILE)
        
        elif choice == 2:
            # view_students()
            std_details = student_details()
            std_details.view_students(JSON_FILE)
        
        elif choice == 3:
            try:
                roll = int(input("Enter student roll to search: "))
            except ValueError:
                print("Please enter a valid roll number.")
                continue

            std_details = student_details()
            std_details.search_student(roll, JSON_FILE)
        
        elif choice == 4:
            # remove_student(name)
            try:
                roll = int(input("Enter student roll to remove: "))
            except ValueError:
                print("Please enter a valid roll number.")
                continue
            std_details = student_details()
            std_details.remove_student(roll, JSON_FILE)

        
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
