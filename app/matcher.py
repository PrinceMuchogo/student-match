from typing import List, Tuple
from app.models import Student

def match_students(students: List[Student]) -> List[Tuple[Student, Student]]:
    matched_pairs = []
    used = set()

    for i in range(len(students)):
        if i in used:
            continue
        for j in range(i + 1, len(students)):
            if j in used:
                continue
            if all([
                students[i].gender == students[j].gender,
                students[i].sleeping_schedule == students[j].sleeping_schedule,
                students[i].cleanliness == students[j].cleanliness,
                students[i].noise_tolerance == students[j].noise_tolerance,
                students[i].smoking == students[j].smoking,
                students[i].study_habits == students[j].study_habits
            ]):
                matched_pairs.append((students[i], students[j]))
                used.update([i, j])
                break
    return matched_pairs
