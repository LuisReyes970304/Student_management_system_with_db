from student_management import StudentManagement
from message import welcome_message_fun, menu_function
from validation import name_validator, option_validator, student_detail_validator, age_validator, status_validator, program_validator


student_list = {}

keep = True
welcome_message_fun()


app = StudentManagement(student_list)
app.synchronize_list_with_db()

while keep:
    menu_function()
    option = option_validator()
    if option == "1":
        print("\nYou chosen: Add New Student")
        name = name_validator()
        age = age_validator()
        program = program_validator()
        status = status_validator()
        app.add_new_student(name=name, age=age, program = program, status = status)
        app.save_data_in_json()
        print("\nNew Student added successfully!\n")

    if option == "2":
        print("\nYou chosen: Check Student List")
        app.check_student_list()

    if option == "3":
        print("\nYou chosen: Find a student")
        detail = student_detail_validator()
        app.find_a_student(detail)

    if option == "4":
        print("\nYou chosen: Update student Information")
        print("Find the student you want to update!\n")
        detail = student_detail_validator()
        student = app.find_a_student(detail)
        if student is not None:
            name = name_validator()
            age = age_validator()
            program = program_validator()
            status = status_validator()
            app.update_student(student ,name=name, age=age, program = program, status = status)
            app.save_data_in_json()

    if option == "5":
        print("\nYou chosen: Delete Student")
        print("Find the student you want to delete!\n")
        detail = student_detail_validator()
        student = app.find_a_student(detail)
        confirmation = input("Are you sure yo want to delete this student? (yes/no): ").lower()
        if confirmation == "yes":
            app.delete_student(student)
            app.save_data_in_json()
            print("\nStudent deleted successfully!")  
        if confirmation != "yes":
            print("Process canceled!")   

    if option == "6":
        keep = False