from typing import List, Dict

# Type alias for a dictionary where keys are strings and values are lists of integers
StudentGrades = Dict[str, List[int]]

def average_grades(grades: StudentGrades) -> Dict[str, str]:
    return {student: sum(marks) / len(marks) for student, marks in grades.items()}

# Using the type alias
grades: StudentGrades = {
    'Alice': [90, 80, 85],
    'Bob': [75, 85, 80]
}

averages = average_grades(grades)
print(averages)  # Output: {'Alice': 85.0, 'Bob': 80.0}