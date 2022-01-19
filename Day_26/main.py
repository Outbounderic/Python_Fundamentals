# new_list = [new_item for item in list if test]

# numbers = range(1,5)
# new_numbers = [number * 2 for number in numbers]
# print(new_numbers)

# new_dict = {new_key:new:value for item in list if test}
# new_dict = {new_key:new:value for (key,value) in dict.items()}
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# students_scores = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score > 60}

# print(students_scores)
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.student)