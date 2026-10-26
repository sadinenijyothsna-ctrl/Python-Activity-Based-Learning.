# Student Marks Matrix Analysis
students = ["Ravi", "Priya", "Raju", "Sita", "Kiran"]
# Marks in 3 subjects: Python, Maths, English
marks = [
    [80, 75, 85],
    [90, 88, 92],
    [60, 65, 70],
    [95, 90, 98],
    [45, 50, 55]
]
print("STUDENT MARKS MATRIX ANALYSIS")
print("-" * 50)

highest_average = -1
topper = ""
for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(marks[i])

    print("\nStudent Name:", students[i])
    print("Python Marks:", marks[i][0])
    print("Maths Marks:", marks[i][1])
    print("English Marks:", marks[i][2])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    if average > highest_average:
        highest_average = average
        topper = students[i]

print("\n" + "-" * 50)
print("Highest Scoring Student:", topper)
print("Highest Average:", round(highest_average, 2))
