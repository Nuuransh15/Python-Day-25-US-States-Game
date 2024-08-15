# with open("weather_data.csv", mode="r") as csv_file:
#     csv_data = csv_file.readlines()
#     print(csv_data)
import numpy as np
# import csv
#
# with open("weather_data.csv", mode="r") as csv_file:
#     data = csv.reader(csv_file)
#     day = []
#     temperature = []
#     condition = []
#     header = None
#     row_num = 0
#     for row in data:
#         if row_num == 0:
#             header = row
#         else:
#             day.append(row[0])
#             temperature.append(int(row[1]))
#             condition.append(row[2])
#         row_num += 1
#
#     print(header)
#     print(day)
#     print(temperature)
#     print(condition)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(len(data[data.day == "Wednesday"]))

# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# print(temp_list)
#
# max_temp = data["temp"].max()
# print(max_temp)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# mon = monday.temp[0] * 9 / 5 + 32
# print(mon)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

unique_colors = list(set(data["Primary Fur Color"]))

data_dict = {
    "Fur Color": [],
    "Count": []
}

for color in unique_colors:
    if color == color:
        data_dict["Fur Color"].append(color)
        data_dict["Count"].append(len(data[data["Primary Fur Color"] == color]))

print(data_dict)
data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

# unique_colors = pd.DataFrame(data["Primary Fur Color"].value_counts())
# unique_colors.to_csv("squirrel_count.csv")
# print(unique_colors)

