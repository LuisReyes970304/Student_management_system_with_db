from time import sleep


welcome_message = """

*************** Welcome to Student Management System ***************

********** This is a simple program that works in console **********

********************** Les't start  with this **********************

"""

invalid_name = """
       **********************************
         Invalid Student name!!!
         Student name cannot be Empty.
       **********************************
         Please try again:

"""

invalid_option = """
       **********************************
         Invalid option!!!
         option has tu be between [1,2,3,4,5,6].
       **********************************
         Please try again:

"""

invalid_detail = """
       **********************************
         Invalid option!!!
       **********************************
         Please try again:

"""

value_error_integer = """
       **********************************
         Invalid student age!!!
         Has to be a postive integer.
       **********************************
         Please try again:   

"""

status = """
       **********************************
         Invalid student status!!!
         Has to be active or inactive.
       **********************************
         Please try again:   

"""

menu = """Select the opction you want.
      1. Add New Student
      2. Check Student List
      3. Find a student
      4. Update student Information
      5. Delete Student
      6. Exit

"""

invalid_program = """
       **********************************
         Invalid option!!!
         student program cannot be empty.
       **********************************
         Please try again:

"""


bye_message = """
****************************************************************

         Thank you for using StudentManagement. Goodbye!

****************************************************************
"""

def welcome_message_fun():
    for i in welcome_message:
        print(i, end="", flush=True)
        sleep(0.01)

def bye_message_function():
    for i in bye_message:
        print(i, end="", flush=True)
        sleep(0.01)

def menu_function():
    for i in menu:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_name_message():     
    for i in invalid_name:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_option_fun():     
    for i in invalid_option:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_detail_fun():     
    for i in invalid_detail:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_integer():     
    for i in value_error_integer:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_status():     
    for i in status:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_program_fun():     
    for i in invalid_program:
        print(i, end="", flush=True)
        sleep(0.01)