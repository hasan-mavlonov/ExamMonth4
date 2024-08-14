from Managers.jsonfilemanager import JSONFIleManager
import logging
import hashlib

filename = 'data/admins.json'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename="../app.log",
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


class AdminManager:
    def __init__(self, username: str):
        self.username = username

    @staticmethod
    @log_decorator
    def show_admin_list() -> list:
        try:
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                yield (f"Full name: {admin['full_name']}\n"
                       f"Username: {admin['username']}\n")
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def check_existence(self) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                if admin['username'] == self.username:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def check_password(self, password: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            for admin in data:
                if admin['username'] == self.username:
                    if admin['password'] == hashed_password:
                        return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def create_admin(self, full_name: str, password: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            data.append({
                'full_name': full_name,
                'username': self.username,
                'password': hashed_password
            })
            if JSONFIleManager(filename).save_data(data):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def change_name(self, new_name: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                if admin['username'] == self.username:
                    admin['full_name'] = new_name
                    JSONFIleManager(filename).save_data(data)
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def change_password(self, new_password: str) -> bool:
        try:
            new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                if admin['username'] == self.username:
                    admin['password'] = new_hashed_password
                    JSONFIleManager(filename).save_data(data)
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def change_username(self, new_username: str) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                if admin['username'] == self.username:
                    admin['username'] = new_username
                    JSONFIleManager(filename).save_data(data)
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    @log_decorator
    def delete_admin(self) -> bool:
        try:
            data = JSONFIleManager(filename).load_data()
            for admin in data:
                if admin('username') == self.username:
                    data.remove(admin)
                    JSONFIleManager(filename).save_data(data)
                    return True
            return False
        except Exception as e:
            print(e)
            return False
