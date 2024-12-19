grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]                                # my_training4
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)                                                                                # сортирую в алфавитном порядке
grades_students = {key: value for key, value in zip(sorted_students, grades)}                                     # сделал словарь с оценками учеников
sum_grades = {key: sum(value) for key, value in grades_students.items()}                                          # cумма символов каждого значения
len_grades = {key: sum(len(str(num)) for num in value) for key, value in grades_students.items()}                 # количество символов каждого значения в списке
students_of_grades = {key: sum_grades[key] / len_grades[key] for key in sum_grades.keys() & len_grades.keys()}    # средний бал всех учеников из списка
print(students_of_grades)