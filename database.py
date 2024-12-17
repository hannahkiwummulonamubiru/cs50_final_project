import sqlite3


def initialize_db():
    """Initialize the SQLite database and create the students table if it doesn't exist."""
    # Connect to the database (this will create 'students.db' if it doesn't exist)
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    # Create the students table if it doesn't already exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grades TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_student_to_db(name, grades_list):
    """Add a new student to the database."""
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    grades_str = ",".join(map(str, grades_list))
    c.execute("INSERT INTO students (name, grades) VALUES (?, ?)", (name, grades_str))
    conn.commit()
    conn.close()

def get_all_students_from_db():
    """Fetch all students from the database as a list of dicts."""
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT id, name, grades FROM students")
    rows = c.fetchall()
    conn.close()
    # Convert rows to list of dicts
    students = []
    for row in rows:
        name = row[1]
        grades_str = row[2]
        grades = [float(g.strip()) for g in grades_str.split(",") if g.strip()]
        students.append({"id": row[0], "name": name, "grades": grades})
    return students

def remove_student_from_db(name):
    """Remove a student by name from the database."""
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT id FROM students WHERE LOWER(name) = LOWER(?)", (name,))
    row = c.fetchone()
    if row is None:
        conn.close()
        raise ValueError(f"Student with name '{name}' not found.")
    c.execute("DELETE FROM students WHERE id = ?", (row[0],))
    conn.commit()
    conn.close()
    return f"Student '{name}' has been removed."

def search_students_in_db(name):
    """Search for students by name and return a list of matching records."""
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT id, name, grades FROM students WHERE LOWER(name) LIKE LOWER(?)", (f"%{name}%",))
    rows = c.fetchall()
    conn.close()

    if not rows:
        raise ValueError(f"No students found matching '{name}'.")

    students = []
    for row in rows:
        grades_str = row[2]
        grades = [float(g.strip()) for g in grades_str.split(",") if g.strip()]
        students.append({"id": row[0], "name": row[1], "grades": grades})
    return students