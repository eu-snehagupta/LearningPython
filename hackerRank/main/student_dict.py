if __name__ == "__main__":
    student = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41.0, 'Harsh': 39.0}
    # student = {'Akriti': 39.0, 'Harsh': 38.0}
    student_score = list(student.values())
    last_score = min(student_score)
    while min(student_score) == last_score:
        student_score.remove(min(student_score))
    second_last_score = min(student_score)
    second_last_students = []
    for element in student:
        if student[element] == second_last_score:
            second_last_students.append(element)
    second_last_students.sort()
    for element in second_last_students:
        print(element)


