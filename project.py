from calculate_median import calculate_median
from search_student import search_student
from remove_student import remove_student

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        raise ValueError("Grades list cannot be empty.")
    return sum(grades) / len(grades)


def determine_grade(average):
    """Determine the letter grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_top_student(student_data):
    """Find the student with the highest average grade."""
    if not student_data:
        raise ValueError("Student data cannot be empty.")
    return max(student_data, key=lambda student: calculate_average(student["grades"]))


def main():
    print("Welcome to the Student Grade Manager!")
    student_data = []

    while True:
        print("\nOptions:")
        print("1. Add a new student")
        print("2. View all students and grades")
        print("3. Find the top student")
        print("4. Search for a student")
        print("5. Remove a student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter student name: ")
            grades_input = input("Enter grades separated by commas (e.g., 85, 90, 78): ")
            try:
                grades = [float(g.strip()) for g in grades_input.split(",")]
                student_data.append({"name": name, "grades": grades})
                print(f"Student {name} added successfully.")
            except ValueError:
                print("Invalid grades input. Please try again.")

        elif choice == "2":
            if not student_data:
                print("No students added yet.")
            else:
                for student in student_data:
                    average = calculate_average(student["grades"])
                    median = calculate_median(student["grades"])
                    grade = determine_grade(average)
                    print(f"{student['name']}: Grades = {student['grades']}, "
                          f"Average = {average:.2f}, Median = {median}, Grade = {grade}")

        elif choice == "3":
            try:
                top_student = get_top_student(student_data)
                top_average = calculate_average(top_student["grades"])
                print(f"Top student: {top_student['name']} with an average of {top_average:.2f}")
            except ValueError as e:
                print(e)


        elif choice == "4":
            key = input("Enter the student's name to search: ")
            try:
                students = search_student(student_data, key)
                print(f"Found {len(students)} student(s) matching '{key}':")
                for student in students:
                    average = calculate_average(student["grades"])
                    print(f" - {student['name']}: Grades = {student['grades']}, Average = {average:.2f}")

            except ValueError as e:

                print(e)

        elif choice == "5":
            name = input("Enter the student's name to remove: ")
            try:
                message = remove_student(student_data, name)
                print(message)
            except ValueError as e:
                print(e)

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

