
import json, os


class file:
    def __init__(self):
        pass
    def create_json_file(self, filename="student_records.json"):
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file, indent=4)
        
    def load_file(self, filename="student_records.json"):
        with open(filename, 'r') as file:
            return json.load(file)
        return []
    def save_file(self, data, filename="student_records.json"):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)