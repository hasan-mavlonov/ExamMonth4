import random
import threading
from Managers.adminmanager import AdminManager
from Managers.teachermanager import TeacherManager
from Managers.groupmanager import GroupManager
from Managers.studentmanager import StudentManager
from Managers.emailmanager import EmailManager


def check_email(email):
    if '@gmail.com' in email:
        return True
    else:
        return False


def check_code(verification_code):
    received_code = input('Enter code that you received: ')
    if received_code == verification_code:
        return True
    else:
        check_code(verification_code)
        return False


def verify_password(email, verification_code):
    receiver = email
    subject = 'Verification Code'
    message = f'Here is your verification code: {verification_code}'
    if EmailManager(receiver, subject, message).send_email():
        print('Email is sent!\n')
        return True


def admin_edit(username) -> None:
    text = """
What do you want to change? 
1. Full Name 
2. Username
3. Password    
4. Exit
            """
    user_input = input(text)
    if user_input == '1':
        new_name = input('Enter new name: ')
        if AdminManager(username).change_name(new_name):
            print("The name successfully changed!")
            admin_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            admin_edit(username)
    elif user_input == '2':
        new_username = input('Enter new username: ')
        if AdminManager(username).change_username(new_username):
            print("The username successfully changed!")
            admin_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            admin_edit(username)
    elif user_input == '3':
        new_password = input('Enter new password: ')
        if AdminManager(username).change_password(new_password):
            print("The password successfully changed!")
            admin_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            admin_edit(username)
    elif user_input == '4':
        admin_crud()
    else:
        print('Invalid input. Try again!')
        admin_edit(username)


def teacher_edit(username) -> None:
    text = """
What do you want to change? 
1. Full Name 
2. Username
3. Password    
4. Exit
            """
    user_input = input(text)
    if user_input == '1':
        new_name = input('Enter new name: ')
        if TeacherManager(username).change_name(new_name):
            print("The name successfully changed!")
            teacher_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            teacher_edit(username)
    elif user_input == '2':
        new_username = input('Enter new username: ')
        if TeacherManager(username).change_username(new_username):
            print("The username successfully changed!")
            teacher_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            teacher_edit(username)
    elif user_input == '3':
        new_password = input('Enter new password: ')
        if TeacherManager(username).change_password(new_password):
            print("The password successfully changed!")
            teacher_crud()
        else:
            print('Unsuccessful attempt. Try again!')
            teacher_edit(username)
    elif user_input == '4':
        teacher_crud()
    else:
        print('Invalid input. Try again!')
        teacher_edit(username)


def admin_crud() -> None:
    text = """
1. Create Admin | full_name, username, password
2. Show Admin list
3. Edit Admin | username
4. Delete Admin | username
5. Exit
"""
    user_input = input(text)
    if user_input == '1':
        full_name = input("Full name: ")
        username = input("Username: ")
        if not AdminManager(username).check_existence():
            password = input("Password: ")
            if AdminManager(username).create_admin(full_name, password):
                print("Admin created successfully")
            else:
                print("Unsuccessful attempt. Try again!")
        else:
            print("Admin with that username already exists")
        admin_crud()
    elif user_input == '2':
        for i in AdminManager.show_admin_list():
            print(i)
        input('Press ANY KEY to go back to the menu: ')
        admin_crud()
    elif user_input == '3':
        username = input('Enter username: ')
        if AdminManager(username).check_existence():
            admin_edit(username)
        else:
            print('Admin with that username does not exist')
            admin_crud()
    elif user_input == '4':
        username = input('Enter username: ')
        if AdminManager(username).check_existence():
            if AdminManager(username).delete_admin():
                print('The admin is successfully deleted')
            else:
                print('Unsuccessful attempt. Try again!')
    elif user_input == '5':
        super_admin_menu()
    else:
        print("Invalid input. Try again!")
        admin_crud()


def teacher_crud() -> None:
    text = """
    1. Create Teacher | full_name, username, password
    2. Show Teacher list
    3. Edit Teacher | username
    4. Delete Teacher | username
    5. Exit
    """
    user_input = input(text)
    if user_input == '1':
        full_name = input("Full name: ")
        username = input("Username: ")
        if not TeacherManager(username).check_existence():
            password = input("Password: ")
            if TeacherManager(username).create_teacher(full_name, password):
                print("Teacher created successfully")
            else:
                print("Unsuccessful attempt. Try again!")
        else:
            print("Teacher with that username already exists")
        teacher_crud()
    elif user_input == '2':
        for i in TeacherManager.show_teacher_list():
            print(i)
        input('Press ANY KEY to go back to the menu: ')
        teacher_crud()
    elif user_input == '3':
        username = input('Enter username: ')
        if TeacherManager(username).check_existence():
            teacher_edit(username)
        else:
            print('Teacher with that username does not exist')
            teacher_crud()
    elif user_input == '4':
        username = input('Enter username: ')
        if TeacherManager(username).check_existence():
            if TeacherManager(username).delete_teacher():
                print('The teacher is successfully deleted')
            else:
                print('Unsuccessful attempt. Try again!')
    elif user_input == '5':
        super_admin_menu()
    else:
        print("Invalid input. Try again!")
        teacher_crud()


def email_menu():
    subject = input('Enter subject: ')
    message = input('Enter message: ')
    text = """
1. Send to all 
2. Send to females
3. Send to males
4. Send to teenagers
5. Send to adults
6. Exit"""
    user_input = input(text)
    if user_input == '1':
        if StudentManager.send_email_to_all_students(subject, message):
            print("Email sent successfully")
        else:
            print("Unsuccessful attempt. Try again!")
        super_admin_menu()
    elif user_input == '2':
        if StudentManager.send_email_to_females(subject, message):
            print("Email sent successfully")
        else:
            print("Unsuccessful attempt. Try again!")
    elif user_input == '3':
        if StudentManager.send_email_to_males(subject, message):
            print("Email sent successfully")
        else:
            print("Unsuccessful attempt. Try again!")
    elif user_input == '4':
        if StudentManager.send_email_to_teenagers(subject, message):
            print("Email sent successfully")
        else:
            print("Unsuccessful attempt. Try again!")
    elif user_input == '5':
        if StudentManager.send_email_to_adults(subject, message):
            print("Email sent successfully")
        else:
            print("Unsuccessful attempt. Try again!")
    else:
        print('Invalid input. Try again!')
        email_menu()
    super_admin_menu()


def super_admin_menu() -> None:
    text = """
1. Admin | CRUD
2. Teacher | CRUD
3. Send email
4. Exit
"""
    user_input = input(text)
    if user_input == "1":
        admin_crud()
    elif user_input == '2':
        teacher_crud()
    elif user_input == '3':
        email_menu()
    elif user_input == '4':
        auth_menu()
    else:
        print("Invalid input. Try again!")
        super_admin_menu()


def group_edit(group_name) -> None:
    text = """
    What do you want to change? 
    1. Group Name 
    2. Max Student
    3. Exit
                """
    user_input = input(text)
    if user_input == '1':
        new_group_name = input('Enter new group name: ')
        if GroupManager(group_name).change_group_name(new_group_name):
            print('Group name successfully changed!')
            groups_crud()
        else:
            print('Unsuccessful attempt. Try again!')
    elif user_input == '2':
        new_max_student = int(input("Enter new max student: "))
        if GroupManager(group_name).change_max_student(new_max_student):
            print('Max student successfully changed!')
        else:
            print('Unsuccessful attempt. Try again!')
    elif user_input == '3':
        groups_crud()
    else:
        print("Invalid input. Try again!")
        group_edit(group_name)


def groups_crud() -> None:
    text = """
1. Create a group | group_name, teacher, max_student, start_time, end_time, status
2. Show group list
3. Edit group 
4. Delete group
5. Exit   
"""
    user_input = input(text)
    if user_input == "1":
        group_name = input("Group name: ")
        for i in TeacherManager.show_teacher_list():
            print(i)
        teacher_name = input("Teacher username: ")
        if TeacherManager(teacher_name).check_existence():
            max_student = int(input("Enter the max number of students: "))
            start_time = input('Start time ')
            end_time = input('End time: ')
            if GroupManager(group_name).create_group(teacher_name, max_student, start_time, end_time):
                print('The group is successfully created')
            else:
                print("Unsuccessful attempt. Try again!")
            groups_crud()
    elif user_input == '2':
        for i in GroupManager.show_group_list():
            print(i)
        input('Press ANY KEY to go back to the menu: ')
        groups_crud()
    elif user_input == '3':
        group_name = input('Enter group name: ')
        if GroupManager(group_name).check_existence():
            group_edit(group_name)
    elif user_input == '4':
        group_name = input('Enter group name: ')
        if GroupManager(group_name).check_existence():
            if GroupManager(group_name).deleted_group():
                print("Successfully deleted!")
            else:
                print('Unsuccessful attempt. Try again!')
            groups_crud()
    elif user_input == '5':
        admin_menu()
    else:
        print('Invalid input. Try again!')
        groups_crud()


def students_crud() -> None:
    text = """
1. Create a student | full_name, gmail, number, gender, age 
2. Show student_list
3. Delete student
4. Exit"""
    user_input = input(text)
    if user_input == '1':
        gmail = input("Gmail: ")
        if check_email(gmail):
            full_name = input("Full name: ")
            number = input("Enter student's number: ")
            gender = str(input("Enter student's gender: "))
            age = input("Enter student's age: ")
            verification_code = random.randint(10000, 99999)
            login = str(random.randint(10000, 99999))
            password = input('Enter password: ')
            verification_code = str(verification_code)
            th1 = threading.Thread(target=verify_password, args=(gmail, verification_code,))
            th1.start()
            if check_code(verification_code):
                print('Your code has been verified!')
                if not StudentManager(gmail).register_a_student(login, password, full_name, number, age, gender):
                    print('Try again!')
                else:
                    print('Successfully registered!')
                    print(f"Login: {login}\nPassword: {password}")
                    students_crud()
            else:
                print('Try again!')
        else:
            print("Invalid email. Try again!")
            students_crud()
    elif user_input == '2':
        for i in StudentManager.show_student_list():
            print(i)
        input('Press ANY KEY to go back to the menu: ')
        students_crud()
    elif user_input == '3':
        login = input("Enter login: ")
        if StudentManager.delete_student(login):
            print('Successfully deleted!')
        else:
            print("Unsuccessful attempt. Try again!")
        students_crud()
    elif user_input == '4':
        admin_menu()
    else:
        print("Invalid input. Try again!")
        students_crud()


def admin_menu() -> None:
    text = """
1. Groups | CRUD
2. Students | CRUD
3. Add student to the group
4. Search by student name
5. Accept Payment
6. Exit  
    """
    user_input = input(text)
    if user_input == "1":
        groups_crud()
    elif user_input == '2':
        students_crud()
    elif user_input == '3':
        group_name = input("Enter group name: ")
        if GroupManager(group_name).check_existence():
            login = input("Enter student login: ")
            if StudentManager.check_existence(login):
                if GroupManager(group_name).add_student(login) and StudentManager.add_group(login, group_name):
                    print('Successfully added!')
                else:
                    print('Unsuccessful attempt. Try again!')
            else:
                print('There is no such a student. Try again!')
        else:
            print("There is no such group. Try again!")
        admin_menu()
    elif user_input == '4':
        login = input('Enter student login: ')
        for i in StudentManager.show_student_list():
            if login in i:
                print(i)
        input('Press ANY KEY to continue')
    elif user_input == '5':
        login = input('Enter student\'s login: ')
        if StudentManager.check_existence(login):
            amount_of_money = float(input('Enter the amount of money you want to add: '))
            if StudentManager.accept_payment(login, amount_of_money):
                print("Money successfully added to the balance!")
            else:
                print("Unsuccessful attempt. Try again!")
        else:
            print('There is no student with such login. Try again!')
        admin_menu()
    elif user_input == '6':
        auth_menu()
    else:
        print("Invalid input. Try again!")
        admin_menu()


def student_menu(login) -> None:
    text = """
1. See all groups
2. See my balance
3. Edit
4. Exit"""
    user_input = input(text)
    if user_input == "1":
        for i in GroupManager.show_group_list():
            print(i)
        input('Press ANY KEY to continue: ')
    elif user_input == '2':
        StudentManager.see_my_balance(login)
        input('Press ANY KEY to continue: ')
    elif user_input == '3':
        gmail = input("Gmail: ")
        if check_email(gmail):
            if StudentManager.delete_student(login):
                full_name = input("Full name: ")
                number = input("Enter student's number: ")
                gender = str(input("Enter student's gender: "))
                age = input("Enter student's age: ")
                verification_code = random.randint(10000, 99999)
                login = str(random.randint(10000, 99999))
                password = input('Enter password: ')
                verification_code = str(verification_code)
                th1 = threading.Thread(target=verify_password, args=(gmail, verification_code,))
                th1.start()
                if check_code(verification_code):
                    print('Your code has been verified!')
                    if not StudentManager(gmail).register_a_student(login, password, full_name, number, age, gender):
                        print('Try again!')
                    else:
                        print('Successfully registered!')
                        print(f"Login: {login}\nPassword: {password}")
                        student_menu(login)
                else:
                    print('Try again!')
        else:
            print("Invalid email. Try again!")
            student_menu(login)
    elif user_input == '4':
        auth_menu()
    else:
        print("Invalid input. Try again!")
        student_menu(login)


def teacher_menu(username) -> None:
    text = """
1. See all groups 
2. See group's students | group_name
3. Start a lesson| group_name
4. Exit
"""
    user_input = input(text)
    if user_input == "1":
        for i in GroupManager.show_group_list():
            print(i)
        input('Press ANY KEY to continue: ')
        teacher_menu(username)
    elif user_input == "2":
        group_name = input("Enter group name: ")
        if GroupManager(group_name).check_existence():

        else:
            print('There is no group named such. Try again!')
    elif user_input == '3':
    elif user_input == '4':
        auth_menu()
    else:
        print('Invalid input. Try again!')
        teacher_menu(username)


def auth_menu() -> (str, None):
    text = """
1. Login | username, password
2. Exit
    """
    user_input = input(text)
    if user_input == '1':
        username = input("Username: ")
        if username == 'super':
            password = input("Password: ")
            if password == 'super':
                super_admin_menu()
        elif AdminManager(username).check_existence():
            password = input("Password: ")
            if AdminManager(username).check_password(password):
                admin_menu()
            elif not AdminManager.check_password():
                print("The password is incorrect. Try again!")
                auth_menu()
        elif StudentManager.check_existence(username):
            password = input("Password: ")
            if StudentManager.check_password(username, password):
                student_menu(username)
        elif TeacherManager(username).check_existence():
            password = input("Password: ")
            if TeacherManager.check_password(password):
                teacher_menu(username)
        else:
            print('There is no user named such. Try again!')
            auth_menu()

    elif user_input == '2':
        exit()
    else:
        print("Invalid input. Try again!")
        auth_menu()


if __name__ == '__main__':
    # empties log file everytime user runs the app
    with open('app.log', 'w'):
        pass
    auth_menu()
