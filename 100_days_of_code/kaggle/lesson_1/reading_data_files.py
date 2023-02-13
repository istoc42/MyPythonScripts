import pandas as pd

reviews = pd.read_csv('kaggle\lesson_1\data.csv')

print(reviews)
print(reviews.shape) # Describes how big the csv is. (no of records, no of columns)
print(reviews.head()) # The .head() method grabs the first five rows

