# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:32:04 2024

@author: Administrator
"""

import pandas

country = pandas.read_csv("country_data.csv")

print(country)
print(country.info())
print(country.describe())

df = pandas.DataFrame({
    'Age': [39, 25, 29, 46, 22, 35, 22, 49, 30,40, 30],
    'Gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'Country':["South Africa", "Botswana", "South Africa","South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
    })

print(df)
print(df['Age'])
print(df['Gender'])
print(df['Country'])

print(df['Age'].min())
print(df['Age'].max())
print(df['Age'].mean())

print(df[df['Age'] > 30])
print(df[1:4])

df['New column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

df.drop(columns= ['New column'], inplace = True)
print(df)

diab = pandas.read_csv("diab_data.csv")

print(diab)
print(diab.info())
print(diab.describe())

column_names = ["A", "B", "C"]

housing = pandas.read_csv("housing_data.csv", names = column_names)

print(housing)
print(housing.info())
print(housing.describe())


insurance = pandas.read_csv("insurance_data.csv", skiprows = 5)

print(insurance)
print(insurance.info())


iris = pandas.read_csv("iris.csv")

print(iris)
print(iris.info())
print(iris.describe())




age = [39, 25, 29, 46, 22, 35, 22, 49, 30,40, 30]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

gender = ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"]

country = ["South Africa", "Botswana", "South Africa","South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]

print(age[:])
print(gender[:])
print(country[:])



person = {'name' : 'John Doe', 'age' : 30, 'address' : '123 Main St.'}
print(person['name'])
print(person.get('age'))
person['phone'] = '555-555-5555'



