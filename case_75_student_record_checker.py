
# Integrated Student Record Consistency Checker

students = [
    ("Ravi", 85, 90),
    ("Priya", 75, 80),
    ("Raju", 110, 70),
    ("Sita", 65, 105),
    ("", 80, 85)
]

print("STUDENT RECORD CONSISTENCY CHECKER")
print("-" * 40)

valid_count = 0
invalid_count = 0

for name, marks, attendance in students:
    print("\nStudent Name:", name if name else "Missing")
    print("Marks:", marks)
    print("Attendance:", attendance, "%")

    if name == "":
        print("Status: Invalid - Name is missing")
        invalid_count += 1
    elif marks < 0 or marks > 100:
        print("Status: Invalid - Marks must be 0 to 100")
        invalid_count += 1
    elif attendance < 0 or attendance > 100:
        print("Status: Invalid - Attendance must be 0 to 100")
        invalid_count += 1
    else:
        print("Status: Valid Record")
        valid_count += 1

print("\n" + "-" * 40)
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)
print("Total Records:", len(students))
