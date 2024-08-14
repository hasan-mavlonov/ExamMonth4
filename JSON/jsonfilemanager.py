import json
import os


class CustomOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class JSONFIleManager:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self) -> list:
        """ loads the data from the file and returns it"""
        if not os.path.exists('../data'):
            os.mkdir('../data')
        if not os.path.exists(self.filename):
            with CustomOpen(self.filename, 'w') as file:
                json.dump([], file, indent=4)
                return []
        else:
            with CustomOpen(self.filename, 'r') as file:
                return json.load(file)

    def save_data(self, data) -> bool:
        """ receives data and saves it in the file"""
        try:
            with CustomOpen(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
                return True
        except Exception as e:
            print(e)
            return False
