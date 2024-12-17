import tkinter as tk
from tkinter import PhotoImage  # For adding images
from tkinter import messagebox
from tkinter import ttk  # Import the ttk module for Treeview

from project import calculate_average, determine_grade, get_top_student
from remove_student import remove_student
from search_student import search_student

# Initialize student data
student_data = []


# Function to create common labels with specific text
def create_label(parent, text, row, column, fg="white", bg="black"):
    label = tk.Label(parent, text=text, fg=fg, bg=bg)
    label.grid(row=row, column=column)
    return label


# Function to create common entry fields
def create_entry(parent, row, column):
    entry = tk.Entry(parent, fg="black", bg="white")
    entry.grid(row=row, column=column)
    return entry


# Function to create buttons with specific text, action, and color scheme
def create_button(parent, text, command, row, column, width=30, bg="#c1ff72", fg="black"):
    button = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, width=width)
    button.grid(row=row, column=column, columnspan=2, pady=5)
    return button


# Functions for GUI options
def add_student():
    def save_student():
        name = name_entry.get()
        grades_input = grades_entry.get()
        try:
            grades = [float(g.strip()) for g in grades_input.split(",")]
            student_data.append({"name": name, "grades": grades})
            messagebox.showinfo("Success", f"Student {name} added successfully.")
            add_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid grades input. Please try again.")

    add_window = tk.Toplevel(root)
    add_window.title("Add New Student")
    add_window.configure(bg="black")

    create_label(add_window, "Student Name:", 0, 0)
    name_entry = create_entry(add_window, 0, 1)

    create_label(add_window, "Grades (comma-separated):", 1, 0)
    grades_entry = create_entry(add_window, 1, 1)

    create_button(add_window, "Save", save_student, 2, 0)


def view_students():
    if not student_data:
        messagebox.showinfo("No Data", "No students added yet.")
        return

    view_window = tk.Toplevel(root)
    view_window.title("All Students and Grades")
    view_window.configure(bg="black")

    # Create a Treeview (table) with columns: Name, Grades, Average, Letter Grade
    columns = ("Name", "Grades", "Average", "Letter Grade")
    treeview = ttk.Treeview(view_window, columns=columns, show="headings", height=10)

    # Define the column headings
    treeview.heading("Name", text="Name")
    treeview.heading("Grades", text="Grades")
    treeview.heading("Average", text="Average")
    treeview.heading("Letter Grade", text="Letter Grade")

    # Adjust column widths
    treeview.column("Name", width=150, anchor="center")
    treeview.column("Grades", width=200, anchor="center")
    treeview.column("Average", width=100, anchor="center")
    treeview.column("Letter Grade", width=120, anchor="center")

    treeview.pack(padx=10, pady=10, expand=True)

    # Insert data into the table
    for student in student_data:
        average = calculate_average(student["grades"])
        letter_grade = determine_grade(average)
        grades_str = ", ".join(map(str, student["grades"]))
        treeview.insert("", "end", values=(student["name"], grades_str, f"{average:.2f}", letter_grade))


def find_top_student():
    try:
        top_student = get_top_student(student_data)
        top_average = calculate_average(top_student["grades"])
        messagebox.showinfo("Top Student",
                            f"Top student: {top_student['name']} with an average of {top_average:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Student data is empty.")


def search_student_gui():
    def perform_search():
        key = search_entry.get()
        try:
            results = search_student(student_data, key)
            result_text = f"Found {len(results)} student(s) matching '{key}':\n"
            for student in results:
                average = calculate_average(student["grades"])
                result_text += f"- {student['name']}: Grades = {student['grades']}, Average = {average:.2f}\n"
            messagebox.showinfo("Search Results", result_text)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    search_window = tk.Toplevel(root)
    search_window.title("Search Student")
    search_window.configure(bg="black")

    create_label(search_window, "Enter Student Name:", 0, 0)
    search_entry = create_entry(search_window, 0, 1)

    create_button(search_window, "Search", perform_search, 1, 0)


def remove_student_gui():
    def perform_remove():
        name = remove_entry.get()
        try:
            message = remove_student(student_data, name)
            messagebox.showinfo("Success", message)
            remove_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Student")
    remove_window.configure(bg="black")

    create_label(remove_window, "Enter Student Name:", 0, 0)
    remove_entry = create_entry(remove_window, 0, 1)

    create_button(remove_window, "Remove", perform_remove, 1, 0)


# Main GUI Setup
root = tk.Tk()
root.title("Student Grade Manager")
root.configure(bg="black")

# Load and display the image
# Load and display the image from a subfolder
try:
    img = PhotoImage(file="assets/GUI.png")  # Use the relative path to your image
    logo_label = tk.Label(root, image=img, bg="black")
    logo_label.pack(pady=10)
except tk.TclError:
    messagebox.showerror("Error", "Image file not found or unsupported format.")

# Menu Options Frame
options_frame = tk.Frame(root, bg="black")
options_frame.pack(pady=20, padx=20)

create_button(options_frame, "Add a new student", add_student, 0, 0)
create_button(options_frame, "View all students and grades", view_students, 1, 0)
create_button(options_frame, "Find the top student", find_top_student, 2, 0)
create_button(options_frame, "Search for a student", search_student_gui, 3, 0)
create_button(options_frame, "Remove a student", remove_student_gui, 4, 0)
create_button(options_frame, "Exit", root.quit, 5, 0)

root.mainloop()
