import statistics

def calculate_median(grades):
    """Calculate the median grade for a student."""
    if not grades:
        raise ValueError("Grades list cannot be empty.")
    return statistics.median(grades)


def search_student(student_data, name):
    """Search for a student by name and return their details."""
    for student in student_data:
        if student["name"].lower() == name.lower():
            return student
    raise ValueError(f"Student with name '{name}' not found.")

def remove_student(student_data, name):
    """Remove a student by name from the system."""
    for student in student_data:
        if student["name"].lower() == name.lower():
            student_data.remove(student)
            return f"Student '{name}' has been removed."
    raise ValueError(f"Student with name '{name}' not found.")

    assert determine_grade(65) == "D"
    assert determine_grade(50) == "F"


