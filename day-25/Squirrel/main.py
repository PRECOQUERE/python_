#얼마나 많은 회색, 시나몬, 검정색 다람쥐가 존재하나

import pandas
data = pandas.read_csv('day-25/Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_black = len(data[data["Primary Fur Color"] == 'Black'])
data_gray = len(data[data["Primary Fur Color"] == 'Gray'])
data_Cinna = len(data[data["Primary Fur Color"] == 'Cinnamon'])

squirrel_color = {
    "color": ['Gray', 'Cinnamon', 'Black'],
    "num": [data_gray, data_Cinna, data_black]
}

df =pandas.DataFrame(squirrel_color)
df.to_csv('day-25/Squirrel/squirrel_count.csv')