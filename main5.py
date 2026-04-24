import os
import csv

#1
def check_files():
    print("Checking file...")

    if not os.path.exists("students.csv"):
        print("Error: students.csv not found.")
        return False

    print("File found: students.csv")

    print("\nChecking output folder...")

    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True


def load_data(filename):
    print("\nLoading data...")
    students = []

    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)

        print(f"Data loaded successfully: {len(students)} students")
        return students

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []
    except Exception as e:
        print("Error while reading file:", e)
        return []


def preview_data(students, n=5):
    print("\nFirst", n, "rows:")
    print("------------------------------")

    for i in range(n):
        s = students[i]
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

    print("------------------------------")


#2
def analyse_countries(students):
    country_counts = {}

    for s in students:
        country = s['country']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1


    top3 = sorted(country_counts.items(), key=lambda x: (-x[1], x[0]))[:3]

    result = {
        "total_students": len(students),
        "total_countries": len(country_counts),
        "top_3": top3,
        "all_countries": country_counts
    }

    return result


#3
def extra_analysis(students):
    print("\n------------------------------")
    print("Lambda / Map / Filter")
    print("------------------------------")

    try:
        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, students))
        print("Students with GPA > 3.5 :", len(high_gpa))

        gpa_values = list(map(lambda s: float(s['GPA']), students))
        print("GPA values (first 5) :", gpa_values[:5])

        good_attendance = list(filter(lambda s: float(s['class_attendance_percent']) > 90, students))
        print("Students attendance > 90% :", len(good_attendance))

    except ValueError:
        print("Error: could not convert some values.")


#MAIN
if check_files():
    students = load_data("students.csv")

    if students:
        preview_data(students)


        result = analyse_countries(students)

        print("\n------------------------------")
        print("Country Analysis")
        print("------------------------------")
        print("Total students :", result["total_students"])
        print("Total countries :", result["total_countries"])

        print("\nTop 3 Countries:")
        for i, (country, count) in enumerate(result["top_3"], 1):
            print(f"{i}. {country} : {count}")

        print("------------------------------")

        extra_analysis(students)
        load_data("wrong_file.csv")