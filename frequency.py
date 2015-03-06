"""
Author: Abraheem Irheem
Frequency counter
"""

letters = []
for x in range(0, 26):
	letters.append(0)

#fileName = raw_input('Enter file name: ')
fileName = 'input.txt'
FILE = open(fileName, 'r+')

while True:
	c = FILE.read(1)
	if c == '':
		break
	index = ord(c) - 97
	if index > 25 or index < 0:
		continue
	letters[index] += 1

FILE.close()

for x in range(0, 26):
	c = chr(x+97)
	p = '%i' % letters[x]
	
	print c + ': ' + '%i' % letters[x]

