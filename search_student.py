def search_student(student_data, name):
    """Search for a student by name and return their details."""
    for student in student_data:
        if student["name"].lower() == name.lower():
            return student
    raise ValueError(f"Student with name '{name}' not found.")
