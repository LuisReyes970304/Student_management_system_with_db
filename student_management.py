import json

#This is the class that manage the CRUD system incharged of creating, updating, loading, uploading and deleting information.
class StudentManagement:
    def __init__(self, student_list: dict, student_db="student_db.json"):
        self.student_list = student_list
        #The student_db is made like this in case the user wants to save the data in a different json file.
        self.student_db = student_db

    #This is the method incharged of loading the existing data in the json file.
    def synchronize_list_with_db(self) -> dict:
        try:
            with open(self.student_db, "r") as file:
                data = json.load(file)
                self.student_list = {int(student_id): student for student_id, student in data.items()}
        except FileNotFoundError:
            with open(self.student_db, "w") as file:
                json.dump(self.student_list, file)
        return self.student_list

    def save_data_in_json(self) -> dict:
        #This is the method incharged of uploading the dict to the json file
        with open(self.student_db, "w") as file:
            json.dump(self.student_list, file)
        return self.student_list
    
    def add_new_student(self, **student_data: dict) -> dict:
        #This method allows creating the new user, which is basically a dict into a dict
        try:
            last_id = next(reversed(self.student_list))
            new_id = last_id + 1
        except StopIteration:
            new_id = 0
        self.student_list[new_id] = student_data
        return {new_id: student_data}
    
    def check_student_list(self) -> dict:
        #This method SHows in console the information of every single student
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
        #This method allows looking for a student based on name or id.
        for student_id, student in self.student_list.items():
            student_name = student["name"]
            student_age = student["age"]
            student_program = student["program"]
            student_status = student["status"]
            if str(student_data) == str(student_id) or student_data == student_name:
                print(f"student id: .......... {student_id}")
                print(f"student name: ........ {student_name}")
                print(f"student age: ......... {student_age}")
                print(f"student course: ...... {student_program}")
                print(f"student status: ...... {student_status}")
                print("****************************************")
                print("")
                return student_id
        print("Student not found or student not exist in database\n")
        return None
    
    def update_student(self, student_id, **student_data: dict):
        #This method allows updating the student information.
        if student_id in self.student_list:
            self.student_list[student_id].update(student_data)
            return self.student_list
        return self.student_list

    def delete_student(self, student_id):
        #This method delete the user selected
        if student_id in self.student_list:
            self.student_list.pop(student_id)
        return self.student_list
    
