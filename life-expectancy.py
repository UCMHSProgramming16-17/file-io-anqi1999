# How much longer am I expected to live, given my sex, age, and country?
import requests

# url
endpoint = 'http://api.population.io:80/1.0/life-expectancy/remaining/'

# parameters
sex = input("Are you male or female? (Apologies for the societal gender norms. The API doesn't take into account the whole spectrum, I'm sorry.) ")
country = input("Which country would you call your home? Or if you'd like to see how fast you'd die in a different country, be my guest. ")
date = input("Today's date? YYYY-MM-DD. ")
age = input("Your age? Could be real or made up. Depends on if you actually care about your estimated time of death. __y__m__d. ")

# assemble
url = endpoint + sex + '/' + country + '/' + date + '/' + age
r = requests.get(url)
print(r)