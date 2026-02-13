students = {}
while True:
    print("\n----- School Data Management System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Show Topper")
    print("6. Show Sections")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print("Roll number already exists!")
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = list(map(int, input("Enter 3 marks: ").split()))
            section = input("Enter Section: ")
            if len(marks) == 3:
                students[roll] = {
                    "name": name,
                    "age": age,
                    "marks": marks,
                    "section": section
                }
                print("Student added successfully!")
            else:
                print("Enter exactly 3 marks!")
    elif choice == "2":
        if not students:
            print("No records found!")
        else:
            for roll, data in students.items():
                print("Roll:", roll)
                print("Name:", data["name"])
                print("Age:", data["age"])
                print("Marks:", data["marks"])
                print("Section:", data["section"])
                print("---------------------")
    elif choice == "3":
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print("Student Found:", students[roll])
        else:
            print("Student not found!")
    elif choice == "4":
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            del students[roll]
            print("Student removed successfully!")
        else:
            print("Student not found!")
    elif choice == "5":
        if students:
            topper = max(students.items(), key=lambda x: sum(x[1]["marks"]))
            print("Topper Roll:", topper[0])
            print("Topper Name:", topper[1]["name"])
            print("Total Marks:", sum(topper[1]["marks"]))
        else:
            print("No records found!")
    elif choice == "6":
        sections = set()
        for data in students.values():
            sections.add(data["section"])
        print("Sections:", sections)
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid choice!")