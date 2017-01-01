# How much longer am I expected to live, given my sex, age, and country?
import requests
import csv
import datetime

# url
endpoint = 'http://api.population.io:80/1.0/life-expectancy/remaining/'

# parameters
# sex = input("Are you male or female? (Apologies for the societal gender norms. The API doesn't take into account the whole spectrum, I'm sorry.) ")
# country = input("Which country would you call your home? Or if you'd like to see how fast you'd die in a different country, be my guest. ")
# date = input("Today's date? If you can remember. Who keeps track of the date these days, anyway? YYYY-MM-DD. ")
# years = input("Your age in years? Could be real or made up. Depends on if you actually care about your estimated time of death. ")
# months = input("And how many months into that age are you? ")
# days = input("And how many days into that month, if you're willing to calculat it? If not, just enter '0' and be done with it. ")

# assemble
# url = endpoint + sex + '/' + country + '/' + date + '/' + years + 'y' + months + 'm' + days + 'd'
# r = requests.get(url)

# life expectancy
# stats = r.json()
# remaining = stats['remaining_life_expectancy']

# PARAMETERS:
# sex
sex = ['male', 'female']

# country
country_url = 'http://api.population.io:80/1.0/countries'
r = requests.get(country_url)
list_countries = r.json()
country = list_countries['countries']

# age
age = []
for num in range(81):
    age.append(num + 'y')

# date
date = datetime.date.today()

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# CSV:
# new csv file
lifechart = open('lifechart.csv', 'w', newline='')

# create the writer
w = csv.writer(lifechart, delimiter=',')

# write to the file
w.writerow(['sex', 'age', 'country', 'life expectancy'])
for gender in sex:
    