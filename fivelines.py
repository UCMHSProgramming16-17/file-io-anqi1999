file = open('lines.txt', 'w')

for l in range(5):
    ask = input('Anything: ')
    file.write(ask + '\n')

file.close()

print('Happy to be working with you! ')