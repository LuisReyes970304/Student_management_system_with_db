from message import invalid_name_message, invalid_option_fun, invalid_detail_fun, invalid_integer, invalid_status, invalid_program_fun


def option_validator():
    validator = True
    while validator:
        option = input("Choose an option: ").strip()
        if not option or option not in ["1", "2", "3", "4", "5", "6"]:
            invalid_option_fun()
            validator = True
        if option: 
            validator = False
    return option


def student_detail_validator():
    validator = True
    while validator:
        option = input("Write the student name or id: ").strip().title()
        if not option:
            invalid_detail_fun()
            validator = True
        if option: 
            validator = False
    return option

def name_validator():
    """This function validates the product name, it makes sure the name is not empty and it capitalizes the first letter of the name."""
    validator = True
    while validator:
        name = input("Write the student name: ").strip().title()
        if not name:
            invalid_name_message()
            validator = True
        if name: 
            validator = False
    return name

def age_validator():
    validator = True
    while validator:
        try:
            age = int(input(f"Write the student age: "))
            if age <= 0: 
                invalid_integer()
                validator = True
            if age > 0:
                validator = False
        except ValueError:
            invalid_integer()
    return age

def status_validator():
    validator = True
    while validator:
        option = input("Write status (active/inactive): ").strip()
        if not option or option not in ["inactive", "active"]:
            invalid_status()
            validator = True
        if option: 
            validator = False
    return option

def program_validator():
    validator = True
    while validator:
        option = input("Write a program: ").strip().capitalize()
        if not option:
            invalid_status()
            validator = True
        if option: 
            validator = False
    return option