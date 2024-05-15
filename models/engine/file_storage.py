import os

class FileStorage:
    __file_path = None
    __objects = dict()
    
    def all(self):
        print("Well this is rather fitting.")
    def new(self, obj):
        pass
    def save(self):
        with open(__file_path, mode="w", encoding="UTF-8") as file_s:
            json.dump( __objects, file_s)
    def reload(self):
        if os.path.exist(__file_path):
            with open(__file_path, mode="r", encoding="UTF-8") as file_s:
                __objects = json.load(file_s)
