def remove_student(student_data, name):
    """Remove a student by name from the system."""
    for student in student_data:
        if student["name"].lower() == name.lower():
            student_data.remove(student)
            return f"Student '{name}' has been removed."
    raise ValueError(f"Student with name '{name}' not found.")
