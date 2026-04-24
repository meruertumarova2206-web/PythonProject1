import os
import csv
import json

#1
print("Checking file...")

if not os.path.exists("students.csv"):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()

print("File found: students.csv")

print("\nChecking output folder...")

if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists")

#2
students = []

with open("students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

print("\nTotal students:", len(students))

print("\nFirst 5 rows:")
print("------------------------------")

for i in range(5):
    s = students[i]
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

print("------------------------------")

#3
country_counts = {}

for s in students:
    country = s['country']
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

print("\n------------------------------")
print("Students by Country")
print("------------------------------")

for country, count in country_counts.items():
    print(f"{country} : {count}")

# Top 3 countries
top3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

print("\n------------------------------")
print("Top 3 Countries:")
print()

for i in range(3):
    print(f"{i+1}. {top3[i][0]} : {top3[i][1]}")

print("------------------------------")

#4
result = {
    "analysis": "Country Analysis",
    "total_students": len(students),
    "total_countries": len(country_counts),
    "top_3_countries": [
        {"country": c, "count": n} for c, n in top3
    ],
    "all_countries": country_counts
}

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("\n==============================")
print("ANALYSIS RESULT")
print("==============================")
print("Analysis : Country Analysis")
print("Total students :", len(students))
print("Total countries :", len(country_counts))

print("\nTop 3 Countries:")
for i in range(3):
    print(f"{i+1}. {top3[i][0]} : {top3[i][1]}")

print("==============================")
print("Result saved to output/result.json")