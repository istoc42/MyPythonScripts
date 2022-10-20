import pandas

squirrel_data = pandas.read_csv(
    "squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(squirrel_data['Primary Fur Color'])

# TODO Get fur color column
fur_color_data = squirrel_data['Primary Fur Color']

# TODO Count each colour
black_fur = fur_color_data.value_counts()["Black"]
cin_fur = fur_color_data.value_counts()["Cinnamon"]
grey_fur = fur_color_data.value_counts()["Gray"]


# TODO Place new data in dataframe
fur_color_dict = {
    "Fur color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_fur, cin_fur, grey_fur]
}
fur_data_frame = pandas.DataFrame(fur_color_dict)

# TODO Save new data frame as csv
fur_data_frame.to_csv("fur_count.csv")
