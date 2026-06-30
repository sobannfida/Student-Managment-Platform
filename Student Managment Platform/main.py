students = []
# Main Function

def main():
    while True:
        try:
            choice = int(input("1.Add Student\n2.Delete Student's Data\n3.Update Student's Data\n4.View Student's Data\n5.Search Student\n6.Exit\n:  "))
            if choice == 1:
                add_student_data()
            elif  choice == 2:
                delete_student_data()
            elif choice == 3:
                update_student_data()
            elif choice == 4:
                view_student_data()
            elif choice == 5:
                search_student()
            elif  choice == 6:
                exit_program()
            else:
                print("Enter Valid Input!")
        except ValueError:
            print("Invalid input. Please enter a choice from 1 to 6")

# Add Student's Data
def add_student_data():

    # Keep asking for a roll number until a unique one is entered
    while True:
        try:
            # Ask user for a roll number
            roll_no = int(input("Enter Student's Roll Number: "))

            # Assume the roll number is unique
            duplicate = False

            # Check every existing student
            for student in students:

                # If another student already has this roll number
                if student["roll_no"] == roll_no:
                    duplicate = True
                    print("Roll Number already exists!")
                    break      # Stop checking further students

            # If no duplicate was found, leave the while loop
            if not duplicate:
                break
        except ValueError:
            print("Enter a valid number with integer data type!")        
    # Now that we have a unique roll number,
    # ask for the remaining student information
    name = input("Enter Student's Name: ")
    class_num = input("Enter Class number: ")
    section = input("Enter Section: ")

    # Create a dictionary to store the student's data
    student = {
        "name": name,
        "roll_no": roll_no,
        "class": class_num,
        "section": section
    }

    # Save the student in the main list
    students.append(student)
# Delete Student's Data
def delete_student_data():
    target = int(input("Enter Student's Roll Number: "))
    found = False
    for student in students:
        if student["roll_no"] == target:
            students.remove(student)
            found = True
            print("Student Deleted Successfully!")
            break
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
            print("Updated Succesfull!")
            break
    if not found:
        print("Roll Number not found!")       

# View Student's Data
def view_student_data():
    if students:
        for student in students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_no']}, Class: {student['class']}, Section: {student['section']}")
    else:
        print("No Student found!")
# Exit
def exit_program():
    quit()
# Search Student
def search_student():
    target = int(input("Enter Student's Roll Number: "))
    found = False
    for student in students:
        if student['roll_no'] == target:
            print(f"Name: {student['name']}, Roll Number: {student['roll_no']}, Class: {student['class']}, Section: {student['section']}")
            found = True
            break
    if not found:
        print("Student Not Found or invalid input")
        

main()
