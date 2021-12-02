from view import display
from model import data_manager


def get_all_students():
    students = data_manager.get_table_from_file("model/files/students.csv")
    display.print_table(students, "Students List:")


def add_new_student():
    user_choice = display.get_inputs(["Name: ",
                                      "Class: ",
                                      "Subject1: ",
                                      "Subject1Mark: ",
                                      "Subject2: ",
                                      "Subject2Mark: ",
                                      "Subject3: ",
                                      "Subject3Mark: ",
                                      "Subject4: ",
                                      "Subject4Mark: "], "Add new student:")
    data_manager.write_new_row("model/files/students.csv", user_choice)
    display.print_message("Student added.")


def choose_operation():
    option = display.get_inputs(["Please enter a number: "], "")[0]
    if option == '1':
        get_all_students()
    elif option == '2':
        add_new_student()
    elif option == '3':
        display.print_message("Update", True)
    elif option == '4':
        display.print_message("Delete", True)
    elif option == '0':
        return False
    else:
        raise KeyError("There is no such option.")
    return True


def handle_submenu():
    options = ["Exit submenu",
               "List students",
               "Add a new student",
               "Update student",
               "Delete student"]
    display.print_menu("Student Classes Submenu", options)


def submenu():
    running = True
    while running:
        handle_submenu()
        try:
            running = choose_operation()
        except KeyError as err:
            display.print_message(str(err), True)
