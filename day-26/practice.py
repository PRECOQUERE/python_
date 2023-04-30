#TODO 리스트 컴프리헨션을 통해 리스트 생성하기
# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# # print(new_list)

# double_list = [n * 2 for n in range(1,4)]
# # print(double_list)

# names = ['Alex', 'Beth', 'caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# #TODO 딕셔너리 컴프리헨션을 사용하는 방법
# import random
# names = ['Alex', 'Beth', 'caroline', 'Dave', 'Eleanor', 'Freddie']

# student_score = {name:random.randint(1, 100) for name in names}
# print(student_score)

# passed_students = {name:score for (name, score) in student_score.items() if score >= 60}
# print(passed_students)

#TODO 판다스 데이터 프레임에서 반복하는 방법
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" :[56, 76, 98]
}

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# for (index, row) in student_dataframe.items():
#     print(row)

for (index, row) in student_dataframe.iterrows():
    print(row)    