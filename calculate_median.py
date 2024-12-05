import statistics

def calculate_median(grades):
    """Calculate the median grade for a student."""
    if not grades:
        raise ValueError("Grades list cannot be empty.")
    return statistics.median(grades)
