# with open("weather_data\weather_data.csv") as data:
#     weather = data.read().splitlines()
#     print(weather)

# import csv

# with open("weather_data\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data\weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()


# def average(lst):
#     return sum(lst) / len(lst)


# average_temp = average(temp_list)
# print("The average temperature this week is " +
#       str(round(average_temp, 1)) + "C")

# max_temp = data['temp'].max()
# print(f'The maximum temperature this week was {max_temp}C')

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# mon_temp = (monday.temp * 9/5) + 32
# print(f"Monday's temperature in Fahrenheit is {float(mon_temp)}F")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 69, 65]
}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_data.csv")
