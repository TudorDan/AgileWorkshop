from view import display
from model import data_manager


def get_all_students():
    students = data_manager.get_table_from_file("model/files/students.csv")
    display.print_table(students, "Students List:")


def choose_operation():
    option = display.get_inputs(["Please enter a number: "], "")[0]
    if option == '1':
        get_all_students()
    elif option == '2':
        display.print_message("'Add a new student' not implemented!", True)
    elif option == '3':
        display.print_message("'Update student' not implemented!", True)
    elif option == '4':
        display.print_message("'Delete student' not implemented!", True)
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
