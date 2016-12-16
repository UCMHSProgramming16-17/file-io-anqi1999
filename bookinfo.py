import requests
# question: "How many pages does my book have?"

# set up api that finds the isbn of a particular book

# set up api that takes the isbn and returns information
# https://openlibrary.org/dev/docs/api/books
url = 'https://openlibrary.org/api/books?'
isbn = input("ISBN: ")
p = {'bibkeys':'ISBN:'+isbn, 'format':'json', 'jscmd':'data'}

# get request
r = requests.get(url, params=p)
print(r.url)

# display information
book = r.json()

bookstats = book['ISBN:'+isbn]

title = bookstats['title']
pages = bookstats['number_of_pages']
authors = bookstats['authors']
date = bookstats['publish_date']
publishers = bookstats['publishers']
subjects = bookstats['subjects']

def pagenumbers():
    if pages <= 100:
        print("%s wrote a cute little story for you! Enjoy.")
    elif 100 < pages <= 300:
        print("%s wrote enough to keep you occupied for at least a few hours!")
    elif 300 < pages <= 700:
        print("This is within the general page count range that bad YA novels have. Good luck. Hopefully %s wrote well.")
    else:
        print("%s must have slaved for years over this book. Appreciate it well. Unless it's like a longer version of Twilight, under which circumstances treat it with its deserved respect and toss it into a dumpster fire.")

if bookstats['subtitle'] in bookstats.keys():
    print('Your book, %s: %s, contains %s pages.' % (title, bookstats['subtitle'], pages))
    pagenumbers() % authors
else:
    print('Your book, %s, contains %s pages.')
    pagenumbers() % authors