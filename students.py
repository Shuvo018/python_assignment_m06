import json
from file_class import file
class student(file):
    def __init__(self, name, roll, email, department):
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department
    def getStudentInfo(self):
        return {"Name": self.name,
                "Roll": self.roll,
                "Email": self.email,
                "Department": self.department}
    
    def setStudentInfo(self, name, roll, email, department):
        pass
        # self.name = name
        # self.roll = roll
        # self.email = email
        # self.department = department

        # self.add_student(JSON_FILE)

    def add_student(self, filename):
        # get previous data
        data = self.load_file(filename)
        
        student = self.getStudentInfo()
        stu_exist = [s for s in data if s["Roll"] == student['Roll']]
        if stu_exist:
            print(f"Error: Roll number {student['Roll']} already exists for another student. ")
            return
        data.append(student)
        #Save students to JSON file
        self.save_file(data, filename)
        print(f"New student added successfully!")


        


