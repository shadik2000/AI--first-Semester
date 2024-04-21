def grade_calculator(assignments: list, bonus_assignment: int, exam: int) -> tuple[bool, int]:
      
    assignments = [0 if assignment is None else assignment for assignment in assignments]
    
    bonus_assignment= 0 if bonus_assignment is None else bonus_assignment

    exam= 0 if exam is None else exam
   
    total_points_combined = sum(assignments) + bonus_assignment + exam
    count_passed_assignments = sum(1 for assignment in assignments if assignment >= 25 or bonus_assignment>=25)
    assignment_points_total = sum(assignments)
    total_percent = (total_points_combined / 11)

    if total_percent >= 87.5:
        total_grade = 1
    elif 75 <= total_percent < 87.5:
        total_grade = 2
    elif 62.5 <= total_percent < 75:
        total_grade = 3
    elif 50 <= total_percent < 62.5:
        total_grade = 4
    else:
        total_grade = 5

    if count_passed_assignments >= 8 and assignment_points_total >= 500 and exam >= 50 :
        return (True, total_grade)
    
    else:
        total_grade=5
        return (False, total_grade)

result = grade_calculator([100,100,100,100,100,100,100,100,100,100], 100, 49)

print(result)