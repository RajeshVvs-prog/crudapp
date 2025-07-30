students = []

def show_menu():
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added!")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for idx, s in enumerate(students):
        print(f"{idx+1}. Name: {s['name']} | Roll: {s['roll']}")

def update_student():
    view_students()
    if not students:
        return
    idx = int(input("Enter student number to update: ")) - 1
    if 0 <= idx < len(students):
        name = input("Enter new name: ")
        roll = input("Enter new roll number: ")
        students[idx]["name"] = name
        students[idx]["roll"] = roll
        print("Student updated!")
    else:
        print("Invalid student number.")

def delete_student():
    view_students()
    if not students:
        return
    idx = int(input("Enter student number to delete: ")) - 1
    if 0 <= idx < len(students):
        students.pop(idx)
        print("Student deleted!")
    else:
        print("Invalid student number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
