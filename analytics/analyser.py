class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):

        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):

        countries = {}

        for s in self.students:

            country = s["country"]

            if country in countries:
                countries[country] += 1
            else:
                countries[country] = 1

        top_3 = sorted(
            countries.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(countries),
            "top_3": top_3,
            "all_countries": list(countries.keys())
        }

    def print_results(self):

        print("\n======================")
        print("COUNTRY ANALYSIS")
        print("======================")

        super().print_results()

        print("======================\n")

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"


class SleepAnalyser(DataAnalyser):

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):

        low_sleep = 0
        high_sleep = 0

        for s in self.students:

            sleep = float(s["sleep_hours"])

            if sleep < 6:
                low_sleep += 1
            else:
                high_sleep += 1

        self.result = {
            "low_sleep": low_sleep,
            "high_sleep": high_sleep
        }

    def print_results(self):

        print("\n======================")
        print("SLEEP ANALYSIS")
        print("======================")

        super().print_results()

        print("======================\n")

    def __str__(self):
        return f"SleepAnalyser: Sleep Analysis, {len(self.students)} students"