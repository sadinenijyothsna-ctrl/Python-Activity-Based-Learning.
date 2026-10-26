
# Student Academic Risk Classification

students = [
    ("Ravi", 85, 90),
    ("Priya", 65, 80),
    ("Raju", 45, 60),
    ("Sita", 30, 40),
    ("Kiran", 55, 45)
]

print("STUDENT ACADEMIC RISK CLASSIFICATION")
print("-" * 45)

for name, marks, attendance in students:
    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Attendance:", attendance, "%")

    if marks < 40 or attendance < 50:
        risk = "High Risk"
    elif marks < 60 or attendance < 75:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    print("Academic Risk:", risk)

print("\nClassification Completed!")
