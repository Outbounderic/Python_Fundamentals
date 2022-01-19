# new_list = [new_item for item in list if test]

# numbers = range(1,5)
# new_numbers = [number * 2 for number in numbers]
# print(new_numbers)

# new_dict = {new_key:new:value for item in list if test}
# new_dict = {new_key:new:value for (key,value) in dict.items()}
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}

print(students_scores)
print(passed_students)