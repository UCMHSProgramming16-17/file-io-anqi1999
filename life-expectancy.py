# How much longer am I expected to live, given my sex, age, and country?
import requests
import math

# url
endpoint = 'http://api.population.io:80/1.0/life-expectancy/remaining/'

# parameters
sex = input("Are you male or female? (Apologies for the societal gender norms. The API doesn't take into account the whole spectrum, I'm sorry.) ")
country = input("Which country would you call your home? Or if you'd like to see how fast you'd die in a different country, be my guest. ")
date = input("Today's date? If you can remember. Who keeps track of the date these days, anyway? YYYY-MM-DD. ")
years = input("Your age in years? Could be real or made up. Depends on if you actually care about your estimated time of death. ")
months = input("And how many months into that age are you? ")
days = input("And how many days into that month, if you're willing to calculat it? If not, just enter '0' and be done with it. ")

# assemble
url = endpoint + sex + '/' + country + '/' + date + '/' + years + 'y' + months + 'm' + days + 'd'
r = requests.get(url)
print(r)

# life expectancy
stats = r.json()
remaining = stats['remaining_life_expectancy']
print(remaining)