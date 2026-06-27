students = []
# Main Function

def main():
    while True:    
        choice = int(input("1.Add Student\n2.Delete Student's Data\n3.Update Student's Data\n4.View Student's Data\n5.Exit\n:  "))
        if choice == 1:
            add_student_data()
        elif  choice == 2:
            delete_student_data()
        elif choice == 3:
            update_student_data()
        elif choice == 4:
            view_student_data()
        elif  choice == 5:
            exit_program()
        else:
            print("Enter Valid Input!")
            again = input("Do you want to try again? y/n").lower()
            if again == "y":
                main()
            else:
                quit()

# Add Student's Data
def add_student_data():
    name = input("Enter Student's Name: ")
    roll_no = int(input("Enter Student's Roll Number: "))
    class_num = input("Enter Class number: ")
    section = input("Enter Section: ")
    student = {
        "name": name,
        "roll_no": roll_no,
        "class": class_num,
        "section": section           
      }
    students.append(student)

# Delete Student's Data
def delete_student_data():
    target = int(input("Enter Student's Roll Number: "))
    found = False
    for student in students:
        if student["roll_no"] == target:
            students.remove(student)
            found = True
            break
            print("Student Deleted Successfully!")
    if not found:
        print("Roll Number not found!")
    print(students)

# Update Student's Data
def update_student_data():
    target = int(input("Enter Student's Roll Number to update: "))
    found = False
    for student in students:
        if student["roll_no"] == target:
            new_name = input("Enter new name for student: ")
            new_class = input("Enter new class for student: ")
            new_section = input("Enter new section for the student: ")
            student["name"] = new_name
            student["class"] = new_class
            student["section"] = new_section
            found = True
            break
    if not found:
        print("Roll Number not found!")       

# View Student's Data
def view_student_data():
    print(students)

# Exit
def exit_program():
    quit()

main()