students = [
    {"name": "Dude", "house": "cool"},
    {"name": "Bro", "house": "woah"},
    {"name": "Man", "house": "woah"},
    {"name": "Luke", "house": "apartment"},
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
