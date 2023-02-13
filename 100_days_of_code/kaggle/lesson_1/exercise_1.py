import pandas as pd


# 1.
fruits = pd.DataFrame(({'Apples': [30], 'Bananas': [21]}))
print('Answer 1:')
print(fruits)
print('-----------------------------------------------------')

# 2.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
print('Answer 2:')
print(fruit_sales)
print('-----------------------------------------------------')

# 3.
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'])
print('Answer 3:')
print(ingredients)
print('-----------------------------------------------------')

# 4. 
# Skipped, can't download the csv at work...

# 5.
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals_csv = animals.to_csv('kaggle\\lesson_1\\animals.csv')