import json
class student:
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
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department

        # self.add_student(JSON_FILE)

    def add_student(self, filename):
        # get previous data
        data = self.load_file(filename)
        
        student = self.getStudentInfo()
        
        data.append(student)
        #Save students to JSON file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"New student added successfully!")

    def load_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)
        return []
        


