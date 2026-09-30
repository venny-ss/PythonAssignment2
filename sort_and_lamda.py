students = [
    ("Ravi", 85),
    ("Sita", 92),
    ("Kiran", 78),
    ("Anu", 95)
]

students.sort(key=lambda x: x[1])

print("Students sorted by marks:")

for student in students:
    print(student)