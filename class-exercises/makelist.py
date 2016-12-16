# open file
file = open('list.txt', 'w')

num = 1
# loop ten times
while num < 11:
    # ask the user for input
    it = input('Favorites? ')
    # write the list item in the form of 'number. item (next line))'
    file.write(str(num) + '. ' + it + '\n')
    num += 1

# close the file
file.close()