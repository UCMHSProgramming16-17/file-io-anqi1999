# import csv
import csv
import random

# open file in write mode
csvfile = open('csvfile.csv', 'w', newline='')

# create the writer
csvwriter = csv.writer(csvfile, delimiter=',')

# write to the file
csvwriter.writerow(['author', 'book'])

bk = input('book: ').lower()
fst = input('first name of author: ').lower()
md = input('middle name of author (if any): ')
lst = input('last name of author: ').lower()

print("type 'stop' at any point to quit the list.")
while bk != 'stop' or fst != 'stop' or md != 'stop' or lst != 'stop':
    if md != '':
        csvwriter.writerow([lst + ', ' + fst + ' ' + md, bk])
    else:
        csvwriter.writerow([lst + ', ' + fst, bk])
    bk = input('book: ').lower()
    fst = input('first name of author: ').lower()
    md = input('middle name of author (if any): ')
    lst = input('last name of author: ').lower()

# close the file
csvfile.close()