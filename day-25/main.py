import csv

with open('day-25/weather_data.csv', mode='r') as file:
    weather_list = csv.reader(file)
    temperatures = []
    
    for row in weather_list :
        temperatures.append(row[1])
    
    for row in range(len(temperatures))
        