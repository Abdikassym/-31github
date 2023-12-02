import pandas

data = pandas.read_csv("weather_data.csv")
# print(data['temp'])

dict_data = data.to_dict()
# print(dict_data)

temp_list = data['temp'].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

# data in columns
# print(data['condition'])
# print(data.condition)

# data in rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] * 9 / 5 + 32
# print(monday_temp)

#Create DataFrame
data_dicta = {
  'students': ["Amy", "Oliver", "Danny"],
  'scores': [76, 82, 55]
}

created_data = pandas.DataFrame(data_dicta)
print(created_data)
created_data.to_csv('created_data.csv')