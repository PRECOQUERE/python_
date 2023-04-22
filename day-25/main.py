import csv

# with open('day-25/weather_data.csv', mode='r') as file:
#     weather_list = csv.reader(file)
#     temperatures = []
    
#     for row in weather_list :
#         if row[1] != 'temp' :
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 04/21

import pandas
# 데이터프레임, 시리즈
data = pandas.read_csv("day-25/weather_data.csv")
# print(type(data))
# print(data['temp'])

# # 딕셔너리로 변환
# data_dict = data.to_dict()
# print(data_dict)

# # 리스트로 변환 
# temp_list = data['temp'].to_list()
# print(temp_list)

# #온도 평균 구하기
# avg_temp = 0
# for temp in temp_list :
#     avg_temp += temp
# avg_temp /= len(temp_list)
# print(f"평균: {avg_temp}")
#  # mean: 의미하다, 평균
# print(f"Pandas 평균: {data['temp'].mean()}")

# #온도 최고값 찾기
# print(f"MAXIMUM: {data['temp'].max()}")

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) 

monday = data[data.day == 'Monday']
print(monday.day)
# print(9/5 * int(monday.temp) + 32)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Jane", "Grace"],
    "scores": ["95", "81", "73"]
}

data = pandas.DataFrame(data_dict)
print(data)