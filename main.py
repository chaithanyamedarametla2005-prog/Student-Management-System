students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == 3:
        roll = input("Enter Roll Number: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True

        if not found:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter Roll Number: ")

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
