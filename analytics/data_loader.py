import csv
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):

        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.students.append(row)

        print(f"Loaded {len(self.students)} students")

    def preview(self):

        print("\nFirst 3 rows:\n")

        for row in self.students[:3]:
            print(row)