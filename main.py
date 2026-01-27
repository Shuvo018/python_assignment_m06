

def menu():
    print("="*8, "MENU", "="*8)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    user_input = -1
    # Handling input error
    try:
        user_input = int(input("Enter your choice: "))
    except Exception as e:
        print("Please enter integer digit. e.g: 1,2,3...")
    # Checking input range
    if user_input<1 or user_input>5:
        print("Please enter number from menu 1 to 5")
        menu()
    return user_input

print(menu())
