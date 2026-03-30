import json

class StudentManagement:
    def __init__(self, student_list: dict, student_db="student_db.json"):
        self.student_list = student_list
        self.student_db = student_db
    
    def synchronize_list_with_db(self):
        try:
            with open(self.student_db, "r") as file:
                data = json.load(file)
                self.student_list.update(data)
        except FileNotFoundError:
            with open(self.student_db, "w") as file:
                json.dump(self.student_list, file)
        return self.student_list

    def save_data_in_json(self):
        with open(self.student_db, "w") as file:
            json.dump(self.student_list, file)
        return self.student_list
    
    def add_new_student(self, **student_data: dict):
        try:
            last_id = int(next(reversed(self.student_list)))
            new_id = last_id + 1
        except StopIteration:
            new_id = 0
        self.student_list[new_id] = student_data
        return student_data
    
    def check_student_list(self):
        for student_id, student in self.student_list.items():
            student_name = student["name"]
            student_age = student["age"]
            student_program = student["program"]
            student_status = student["status"]
            print(f"student id: .......... {student_id}")
            print(f"student name: ........ {student_name}")
            print(f"student age: ......... {student_age}")
            print(f"student course: ...... {student_program}")
            print(f"student status: ...... {student_status}")
            print("****************************************")
            print("")
        return self.student_list
    
    def find_a_student(self, student_data: str):
        for student_id, student in self.student_list.items():
            student_name = student["name"]
            student_age = student["age"]
            student_program = student["program"]
            student_status = student["status"]
            if student_data == str(student_id) or student_data == student_name:
                print(f"student id: .......... {student_id}")
                print(f"student name: ........ {student_name}")
                print(f"student age: ......... {student_age}")
                print(f"student course: ...... {student_program}")
                print(f"student status: ...... {student_status}")
                print("****************************************")
                print("")
                return self.student_list
        print("Student not found or student not exist in database\n")
        return None
    
    def update_student(self, student_id, **student_data: dict):
        if student_id in self.student_list:
            self.student_list[student_id] = student_data
        print(self.student_list)

    def delete_student(self, student_data: str):
        for student_id, student in self.student_list.items():
            student_name = student["name"]
            if student_data == str(student_id) or student_data == student_name:
                self.student_list.pop()
        pass