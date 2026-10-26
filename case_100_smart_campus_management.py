# Comprehensive Smart Campus Management Simulation

students = [
    ("Ravi", 90),
    ("Priya", 75),
    ("Raju", 45),
    ("Sita", 95)
]

library_books = [
    ("Python Basics", True),
    ("Web Development", False),
    ("AI Fundamentals", True)
]

classrooms = [
    ("Room 101", "Available"),
    ("Room 102", "Occupied"),
    ("Room 103", "Available")
]

print("SMART CAMPUS MANAGEMENT SYSTEM")
print("=" * 40)

# Student Attendance Report
print("\nSTUDENT ATTENDANCE REPORT")
present_count = 0

for name, attendance in students:
    print(name, "-", attendance, "% attendance")

    if attendance >= 75:
        print("Status: Eligible")
        present_count += 1
    else:
        print("Status: Low Attendance")

# Library Report
print("\nLIBRARY BOOK REPORT")
available_books = 0

for book, available in library_books:
    if available:
        print(book, "- Available")
        available_books += 1
    else:
        print(book, "- Issued")

# Classroom Report
print("\nCLASSROOM STATUS REPORT")
available_rooms = 0

for room, status in classrooms:
    print(room, "-", status)

    if status == "Available":
        available_rooms += 1

# Final Summary
print("\n" + "=" * 40)
print("CAMPUS SUMMARY")
print("Total Students:", len(students))
print("Students Eligible by Attendance:", present_count)
print("Available Library Books:", available_books)
print("Available Classrooms:", available_rooms)
print("Campus Report Completed!")
