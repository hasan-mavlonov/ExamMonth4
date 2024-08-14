from Managers.jsonfilemanager import JSONFIleManager
from Managers.emailmanager import EmailManager
from Managers.messagemanager import MessageManager
import logging
import hashlib

filename = 'data/students.json'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    datefmt='%d-%m-%y %H:%M:%S'
                    )


def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            message = f'Function: {func} Args: {args} Result: {result}'
            logger.info(message)
            return result
        except Exception as e:
            message = f'Function: {func} Args: {args} Error: {e}'
            logger.error(message)
            return e

    return wrapper


logger = logging.getLogger(__name__)


class StudentManager:
    def __init__(self, email: str):
        self.email = email

    def register_a_student(self, login: str, password: str, full_name: str, number: str, age: str, gender: str) -> bool:
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            data = JSONFIleManager(filename).load_data()
            data.append({
                'gmail': self.email,
                'login': login,
                'full_name': full_name,
                'age': age,
                'number': number,
                'gender': gender,
                'password': hashed_password,
                'groups': [],
                'balance': 0
            })
            if JSONFIleManager(filename).save_data(data):
                return True
        except Exception as e:
            print(e)
            return False

    def check_email(self):
        try:
            data = JSONFIleManager(filename).load_data()
            for user in data:
                if user['gmail'] == self.email:
                    return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def check_password(login, password):
        try:
            data = JSONFIleManager(filename).load_data()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            for user in data:
                if user['login'] == login:
                    if user['password'] == hashed_password:
                        return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    @log_decorator
    def show_student_list() -> list:
        try:
            data = JSONFIleManager(filename).load_data()
            for student in data:
                yield (f"Full name: {student['full_name']}\n"
                       f"Username: {student['login']}\n"
                       f"Gmail: {student['gmail']}\n")
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def delete_student(login: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for student in data:
                if student['login'] == login:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def accept_payment(login, amount_of_money: float):
        try:
            data = JSONFIleManager(filename).load_data()
            amount_of_money = amount_of_money * 100
            for student in data:
                if student['login'] == login:
                    student['balance'] = student['balance'] * 100
                    student['balance'] += amount_of_money
                    student['balance'] = student['balance'] / 100
                    if JSONFIleManager(filename).save_data(data):
                        return True
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def check_existence(login: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for student in data:
                if student['login'] == login:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def send_email_to_all_students(subject, message):
        try:
            if MessageManager(message).create_message():
                data = JSONFIleManager(filename).load_data()
                done = True
                for student in data:
                    if EmailManager(student['gmail'], subject, message).send_email():
                        if done:
                            if MessageManager(message).add_receiver(student['gmail']):
                                done = True
                        if not done:
                            print('Error occurred!')
                            return False
                if done:
                    return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @staticmethod
    def send_email_to_males(subject, message):
        try:
            if MessageManager(message).create_message():
                data = JSONFIleManager(filename).load_data()
                done = True
                for student in data:
                    if student['gender'] == 'male':
                        if EmailManager(student['gmail'], subject, message).send_email():
                            if done:
                                if MessageManager(message).add_receiver(student['gmail']):
                                    done = True
                            if not done:
                                print('Error occurred!')
                                return False
                if done:
                    return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @staticmethod
    def send_email_to_females(subject, message):
        try:
            if MessageManager(message).create_message():
                data = JSONFIleManager(filename).load_data()
                done = True
                for student in data:
                    if student['gender'] == 'female':
                        if EmailManager(student['gmail'], subject, message).send_email():
                            if done:
                                if MessageManager(message).add_receiver(student['gmail']):
                                    done = True
                            if not done:
                                print('Error occurred!')
                                return False
                if done:
                    return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @staticmethod
    def send_email_to_adults(subject, message):
        try:
            if MessageManager(message).create_message():
                data = JSONFIleManager(filename).load_data()
                done = True
                for student in data:
                    if student['age'] >= 18:
                        if EmailManager(student['gmail'], subject, message).send_email():
                            if done:
                                if MessageManager(message).add_receiver(student['gmail']):
                                    done = True
                            if not done:
                                print('Error occurred!')
                                return False
                if done:
                    return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @staticmethod
    def send_email_to_teenagers(subject, message):
        try:
            if MessageManager(message).create_message():
                data = JSONFIleManager(filename).load_data()
                done = True
                for student in data:
                    if student['age'] <= 18:
                        if EmailManager(student['gmail'], subject, message).send_email():
                            if done:
                                if MessageManager(message).add_receiver(student['gmail']):
                                    done = True
                            if not done:
                                print('Error occurred!')
                                return False
                if done:
                    return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @staticmethod
    def add_group(login, group_name):
        try:
            data = JSONFIleManager(filename).load_data()
            for student in data:
                if student['login'] == login:
                    groups = student['groups']
                    groups.append(group_name)
                    student['groups'] = groups
                    if JSONFIleManager(filename).save_data(data):
                        return True
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False
    @staticmethod
    def see_my_balance(login):
        try:
            data = JSONFIleManager(filename).load_data()
            for student in data:
                if student['login'] == login:
                    print(student['balance'])
                    return True
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False
