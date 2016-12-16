import csv

# open the file in writing mode
csvfile = open('csvpractice.csv', 'w', newline='')

# create the writer
csvwriting = csv.writer(csvfile, delimiter=',')

# write to the file
csvwriting.writerow(['first half', 'second half', 'compound word', 'definition'])

print("Let's make up compound words! Now is your time to create your own compound dictionary. :D")

n = 0
while n < 5:
    first = input("First half of your new word: ")
    second = input("Second half of your new word: ")
    definition = input("Definition of your new word: ")
    csvwriting.writerow([first, second, first + second, definition])
    print("Your word has been logged into the dictionary!")
    n += 1
