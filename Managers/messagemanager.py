from ExamMonth4.Managers.jsonfilemanager import JSONFIleManager
import datetime
import logging

filename = 'data/messages.json'

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


class MessageManager:
    def __init__(self, message):
        self.message = message

    def create_message(self):
        try:
            data = JSONFIleManager(filename).load_data()
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data.append({
                'message': self.message,
                'new_receivers': [],
                'old_receivers': [],
                'time': time
            })
            JSONFIleManager(filename).save_data(data)
            return True
        except Exception as e:
            print(e)
            return False

    def add_receiver(self, receiver):
        data = JSONFIleManager(filename).load_data()
        for messages in data:
            if messages['message'] == self.message:
                receivers = messages['new_receivers']
                receivers.append(receiver)
                messages['new_receivers'] = receivers
        if JSONFIleManager(filename).save_data(data):
            return True

    @staticmethod
    def show_message_with_time():
        try:
            data = JSONFIleManager(filename).load_data()
            for message in data:
                print(f"""
Message: {message['message']}
Time: {message['time']}
""")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def show_messages_by_email(email):
        try:
            data = JSONFIleManager(filename).load_data()
            exist = False
            for message in data:
                new_users = message['new_receivers']
                old_users = message['old_receivers']
                if email in new_users:
                    print(f"""
Message: {message['message']}
Time: {message['time']}
                    """)
                    new_users.remove(email)
                    old_users.append(email)
                    message['new_receivers'] = new_users
                    message['old_receivers'] = old_users
                    if JSONFIleManager(filename).save_data(data):
                        exist = True
            if exist:
                return True
            if not exist:
                return False
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def show_messages_by_read_email(email):
        try:
            data = JSONFIleManager(filename).load_data()
            exist = False
            for message in data:
                old_users = message['old_receivers']
                if email in old_users:
                    print(f"""
Message: {message['message']}
Time: {message['time']}
                    """)
                    exist = True
            if exist:
                return True
            if not exist:
                return False
        except Exception as e:
            print(e)
            return False
