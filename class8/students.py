# with open("names.csv", "r") as file:
#     for line in file:
#         name, adjective = line.rstrip().split(",")
#         print(f"hello {name}, you are {adjective}")

students = []
with open("names.csv", "r") as file:
    for line in file:
        name, adjective = line.rstrip().split(",")
        students.append({"name": name, "adjective": adjective})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['adjective']}")
