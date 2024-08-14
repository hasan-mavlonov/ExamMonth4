from Managers.jsonfilemanager import JSONFIleManager
import logging
import hashlib

filename = 'data/groups.json'

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


class GroupManager:
    def __init__(self, group_name):
        self.group_name = group_name

    @log_decorator
    def check_existence(self) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def create_group(self, teacher: str, max_student: int, start_time: str, end_time: str):
        try:
            data = JSONFIleManager(filename).load_data()
            data.append({
                'group_name': self.group_name,
                'teacher': teacher,
                'max_student': max_student,
                'start_time': start_time,
                'end_time': end_time,
                'status': True,
                'students': []
            })
            if JSONFIleManager(filename).save_data(data):
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    @log_decorator
    def show_group_list() -> list:
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                yield (f"Group Name: {group['group_name']}\n"
                       f"Teacher: {group['teacher']}\n"
                       f"Students: {group['students']}")
        except Exception as e:
            print(e)
            return False

    def change_group_name(self, new_group_name: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    group['group_name'] = new_group_name
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def change_max_student(self, new_max_student: int) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    group['max_student'] = new_max_student
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def deleted_group(self):
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    data.remove(group)
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def add_student(self, login):
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    students = group['students']
                    students.append(login)
                    group['students'] = students
                    if JSONFIleManager(filename).save_data(data):
                        return True
            return False
        except Exception as e:
            print(e)
            return False

    def show_group_students(self):
        try:
            data = JSONFIleManager(filename).load_data()
            for group in data:
                if group['group_name'] == self.group_name:
                    students = group['students']
                    for student in students:
                        yield student
        except Exception as e:
            print(e)
            return False
