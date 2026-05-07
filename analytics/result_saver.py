import json
class ResultSaver:

    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def save_json(self):

        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

        print(f"Result saved to {self.filename}")