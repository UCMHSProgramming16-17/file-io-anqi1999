# How much longer am I expected to live, given my sex, age, and country?
import requests
import csv
import datetime

# PARAMETERS:
# sex
sex = ['male', 'female']

# country
country = input('Country? ')

# age
age = []
for num in range(81):
    age.append(str(num) + 'y')

# date
date = str(datetime.date.today())

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# CSV:
# new csv file
lifechart = open('lifechart.csv', 'w', newline='')

# create the writer
w = csv.writer(lifechart, delimiter=',')

# write to the file
w.writerow(['age', 'sex', 'life remaining, in years'])
for a in age:
    for s in sex:
        # get the remaining life expectancy
        endpoint = 'http://api.population.io:80/1.0/life-expectancy/remaining/'
        url = endpoint + s + '/' + country + '/' + date + '/' + a
        r = requests.get(url)
        stats = r.json()
        remaining = stats['remaining_life_expectancy']
        # write each to the file
        w.writerow([a, s, remaining])
            
# close file
lifechart.close()