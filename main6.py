import os
import csv
import json
#1
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if not os.path.exists(self.filename):
            print(f"Error: {self.filename} not found.")
            return False

        print(f"File found: {self.filename}")
        return True

    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")
#2
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")

        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.students = list(reader)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview(self, n=5):
        print(f"\nFirst {n} rows:")
        print("------------------------------")

        for i in range(min(n, len(self.students))):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("------------------------------")
#3
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        country_counts = {}

        for s in self.students:
            country = s['country']
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        top3 = sorted(country_counts.items(), key=lambda x: (-x[1], x[0]))[:3]

        self.result = {
            "total_countries": len(country_counts),
            "country_counts": country_counts,
            "top_3": top3
        }

        return self.result

    def print_results(self):
        print("\n------------------------------")
        print("Country Analysis")
        print("------------------------------")

        print("Total countries :", self.result["total_countries"])

        print("Top 3 Countries:")
        for i, (country, count) in enumerate(self.result["top_3"], 1):
            print(f"{i}. {country} : {count}")

        print("------------------------------")
#4
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)

            print(f"\nResult saved to {self.output_path}")

        except Exception as e:
            print("Error saving file:", e)
#5
def main():
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()

    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()
if __name__ == "__main__":
    main()