def search_student(student_data, key):
    """
    Search for students by name containing the given key and return their details.
    """
    results = [student for student in student_data if key.lower() in student["name"].lower()]
    if not results:
        raise ValueError(f"No students found with name containing '{key}'")
    return results