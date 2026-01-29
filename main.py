import json
import os
from datetime import datetime
from students import student
from student_details import student_details
from file_class import file
import re

JSON_FILE = "student_records.json"

    
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
        
    
    if user_input < 1 or user_input > 5:
        print("Please enter number from menu 1 to 5")
    elif user_input > 0 and user_input < 6:
        return user_input
    return -1



def main():
    # Create JSON file on startup
    file_handler = file()
    file_handler.create_json_file()
    
    
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
            # Error handling
            if not name or not roll or not email or not dept:
                print("All fields are required")
                continue
            if name.isdigit():
                print("Name cannot be numeric. Please try again.")
                continue
            if len(name) > 25:
                print("Name is too long. Please try again.")
                continue


            if roll < 0:
                print("Roll number cannot be negative. Please try again.")
                continue
            if roll > 99999:
                print("Roll number is too large. Please try again.")
                continue
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.match(pattern, email):
                print("Invalid email format. Please try again.")
                continue
            
            if dept.isdigit():
                print("Department cannot be numeric. Please try again.")
                continue
            if len(dept) > 35:
                print("Department name is too long. Please try again.")
                continue
            
            std = student(name, roll, email, dept)
            std.add_student(JSON_FILE)
        
        elif choice == 2:
            # view_students()
            std_details = student_details()
            std_details.view_students(JSON_FILE)
        
        elif choice == 3:
            # search_student
            try:
                roll = int(input("Enter student roll to search: "))
            except ValueError:
                print("Please enter a valid roll number.")
                continue
            if roll < 0:
                print("Roll number cannot be negative. Please try again.")
                continue
            if roll > 99999:
                print("Roll number is too large. Please try again.")
                continue
            std_details = student_details()
            std_details.search_student(roll, JSON_FILE)
        
        elif choice == 4:
            # remove_student
            try:
                roll = int(input("Enter student roll to remove: "))
            except ValueError:
                print("Please enter a valid roll number.")
                continue
            if roll < 0:
                print("Roll number cannot be negative. Please try again.")
                continue
            if roll > 99999:
                print("Roll number is too large. Please try again.")
                continue
            
            std_details = student_details()
            std_details.remove_student(roll, JSON_FILE)

        
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
