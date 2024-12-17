import pytest
from main import calculate_average, determine_grade, get_top_student
from calculate_median import calculate_median
from search_student import search_student
from remove_student import remove_student

def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 80
    assert calculate_average([100]) == 100
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_median():
    assert calculate_median([90, 80, 70]) == 80
    assert calculate_median([85, 75, 95, 70]) == 80
    with pytest.raises(ValueError):
        calculate_median([])


def test_determine_grade():
    assert determine_grade(95) == "A"
    assert determine_grade(85) == "B"
    assert determine_grade(75) == "C"
    assert determine_grade(65) == "D"
    assert determine_grade(50) == "F"


def test_get_top_student():
    students = [
        {"name": "Alice", "grades": [95, 90, 85]},
        {"name": "Bob", "grades": [80, 85, 88]},
        {"name": "Charlie", "grades": [70, 75, 72]}
    ]
    assert get_top_student(students)["name"] == "Alice"
    with pytest.raises(ValueError):
        get_top_student([])


def test_search_student():
    students = [
        {"name": "Alice", "grades": [95, 90, 85]},
        {"name": "Bob", "grades": [80, 85, 88]}
    ]
    assert search_student(students, "Alice") == {"name": "Alice", "grades": [95, 90, 85]}
    with pytest.raises(ValueError):
        search_student(students, "Charlie")


def test_remove_student():
    students = [
        {"name": "Alice", "grades": [95, 90, 85]},
        {"name": "Bob", "grades": [80, 85, 88]}
    ]
    assert remove_student(students, "Alice") == "Student 'Alice' has been removed."
    assert len(students) == 1
    with pytest.raises(ValueError):
        remove_student(students, "Charlie")
