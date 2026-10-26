# Smart Classroom Timetable Allocation

timetable = [
    ("Monday", "09:00 AM", "Python", "Room 101"),
    ("Monday", "10:00 AM", "Mathematics", "Room 101"),
    ("Monday", "09:00 AM", "English", "Room 102"),
    ("Tuesday", "09:00 AM", "Python Lab", "Room 101"),
    ("Tuesday", "09:00 AM", "AI", "Room 101")
]

print("SMART CLASSROOM TIMETABLE")
print("-" * 45)

conflicts = 0

for i in range(len(timetable)):
    day, time, subject, room = timetable[i]

    print("\nDay:", day)
    print("Time:", time)
    print("Subject:", subject)
    print("Room:", room)

    conflict_found = False

    for j in range(i):
        old_day, old_time, old_subject, old_room = timetable[j]

        if day == old_day and time == old_time and room == old_room:
            conflict_found = True

    if conflict_found:
        print("Status: Conflict - Room already allocated")
        conflicts += 1
    else:
        print("Status: Available")

print("\n" + "-" * 45)
print("Total Timetable Entries:", len(timetable))
print("Room Conflicts:", conflicts)
print("Timetable Check Completed!")
