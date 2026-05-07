import os
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):

        if os.path.exists(self.filename):
            print("File found")
        else:
            print("File not found")

    def create_output_folder(self):

        if not os.path.exists("output"):
            os.makedirs("output")

        print("Output folder ready")