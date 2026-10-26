# Advanced String-Based Registration Record Analyzer
students = [
    ("REG101", "Ravi"),
    ("REG102", "Priya"),
    ("REG103", ""),
    ("REG102", "Raju"),
    ("ABC104", "Sita")
]
seen_ids = []
valid_count = 0
invalid_count = 0
duplicate_count = 0
print("REGISTRATION RECORD ANALYZER")
print("-" * 40)
for reg_id, name in students:
    print("\nRegistration ID:", reg_id)
    print("Student Name:", name if name else "Missing")
    if reg_id in seen_ids:
        print("Status: Duplicate Registration ID")
        duplicate_count += 1

    elif not reg_id.startswith("REG"):
        print("Status: Invalid Registration ID")
        invalid_count += 1
        seen_ids.append(reg_id)

    elif name.strip() == "":
        print("Status: Missing Student Name")
        invalid_count += 1
        seen_ids.append(reg_id)

    else:
        print("Status: Valid Record")
        valid_count += 1
        seen_ids.append(reg_id)

print("\n" + "-" * 40)
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)
print("Duplicate Records:", duplicate_count)
print("Total Records:", len(students))
