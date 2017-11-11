name = ''
while not name != '':
	print('Enter your name:')
	name = input()
	print('How many guests will you have?')
	numOfGuests = int(input())
	if numOfGuests != 0:
		print('Be sure to have enough room for all your guests.')
print('Done')
