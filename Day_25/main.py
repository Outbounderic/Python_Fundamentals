# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp = monday_temp * 9/5 + 32
# print(monday_temp)
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_list = data["Primary Fur Color"].to_list()
squirrel_dict = {
    "color": [],
    "count": []
}

gray_count = 0
cinnamon_count = 0
black_count = 0

for fur_color in fur_list:
    if fur_color == "Gray":
        gray_count += 1
    elif fur_color == "Cinnamon":
        cinnamon_count += 1
    elif fur_color == "Black":
        black_count += 1

squirrel_dict["color"] = ["gray", "cinnamon", "black"]
squirrel_dict["count"] = [gray_count, cinnamon_count, black_count]

squirrel_color_count = pandas.DataFrame(squirrel_dict)
squirrel_color_count.to_csv("squirrel_color_data.csv")
















