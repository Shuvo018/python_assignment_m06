
import json
import students
class student_details(students.student):
    def __init__(self):
        pass

    def view_students(self, filename):
        data = self.load_file(filename)

        if not data:
            print("Database is empty")
            return
        print("\n" + "="*60)
        print(f"{'Name':<20} {'Roll':<10} {'Email':<20} {'Department':<15}")
        print("="*60)
        for stu in data:
            print(f"{stu['Name']:<20} {stu['Roll']:<10} {stu['Email']:<20} {stu['Department']:<15} ")
        
        print("="*60 + "\n")

    def search_student(self, roll, filename):
        data = self.load_file(filename)

        results = [s for s in data if s["Roll"] == roll]
        if results:
            for stu in results:
                print(f"Name: {stu['Name']}, Roll: {stu['Roll']}, Email: {stu['Email']}, Department: {stu['Department']}")
        else:
            print(f"No student found with roll {roll} ")
    def remove_student(self, roll, filename):
        data = self.load_file(filename)
        initial_count = len(data)
        data = [s for s in data if s["Roll"] != roll]
        if len(data) < initial_count:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Student with roll {roll} removed successfully!")
        else:
            print(f"No student found with roll {roll}")
