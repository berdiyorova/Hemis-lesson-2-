from Programs.Hemis.logs import log_settings
from Programs.Hemis.users.common import login, UserTypes, add_user
from Programs.Hemis.utils.subjects import add_subject


def print_menu(user_type):
    return f"""
    1. Add {user_type}
    2. Delete {user_type}
    3. Edit {user_type}
    4. Show {user_type}s
    5. Search {user_type}
    6. Back
    """


def admin_teacher_menu():
    print(print_menu(user_type="teacher"))
    choice = input("Enter your choice: ")
    if choice == "1":
        if add_user(user_type=UserTypes.TEACHER.value):
            print("Successfully added new teacher")
            admin_teacher_menu()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        show_admin_menu()
    else:
        print("Wrong choice !")
        admin_teacher_menu()


def admin_student_menu():
    print(print_menu(user_type="student"))
    choice = input("Enter your choice: ")
    if choice == "1":
        if add_user(user_type=UserTypes.STUDENT.value):
            print("Successfully added new student")
            admin_teacher_menu()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Wrong choice !")
        show_admin_menu()


def admin_subjects_menu():
    print(print_menu(user_type="subject"))
    choice = input("Enter your choice: ")
    if choice == "1":
        if add_subject():
            print("Successfully added new subject")
            admin_subjects_menu()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Wrong choice !")
        show_admin_menu()


def admin_lessons_menu():
    print(print_menu(user_type="lesson"))
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Wrong choice !")
        show_admin_menu()


def admin_groups_menu():
    print(print_menu(user_type="group"))
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Wrong choice !")
        show_admin_menu()


def show_admin_menu():
    print("""
    1. Teachers
    2. Students
    3. Subjects
    4. Groups
    5. Lessons
    6. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        admin_teacher_menu()
    elif choice == "2":
        admin_student_menu()
    elif choice == "3":
        admin_subjects_menu()
    elif choice == "4":
        admin_groups_menu()
    elif choice == "5":
        admin_lessons_menu()
    elif choice == "6":
        pass
    else:
        print("Wrong choice !")
        show_admin_menu()


def show_teacher_menu():
    print("Welcome to the teacher menu")


def show_student_menu():
    print("Welcome to the student menu")


def show_auth() -> None:
    print("""
    1. Login
    2. Exit
    """)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        user = login()
        if not user:
            print("Invalid username or password")
        elif user['user_type'] == UserTypes.ADMIN.value:
            show_admin_menu()
        elif user['user_type'] == UserTypes.TEACHER.value:
            show_teacher_menu()
        elif user['user_type'] == UserTypes.STUDENT.value:
            show_student_menu()

    else:
        print("Goodbye !")
        return


if __name__ == "__main__":
    log_settings()
    show_auth()
