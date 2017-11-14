def comma(aList):
	for i in range(len(aList) -1):
		print(aList[i], end = ', ')
	print('and ' + aList[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)
