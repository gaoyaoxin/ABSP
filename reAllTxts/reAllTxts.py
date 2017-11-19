#! python3
# reAllTxts.py - Open all .txt files in the folder and find all lines fitting user input regex.

import os, re

print("Please input a Regex")
inputRegex = input()
Regex = re.compile(inputRegex)

fileList = os.listdir()
for i in range(fileList)
	text = open('%s.txt' % (fileList[i]))
	textLines = text.readlines()

# TODO: print out the !lines! with fitted regex

	matches = []
	for groups in Regex.findall(text):
		regexFound = ''.join(groups[0])
		matches.append(regexFound)
	if len(matches) > 0:
		for i in range(len(matches)):
		# this need to be fixed. print('Enter a/an %s:' % (matches[i].lower()))
		print('Enter a/an' + matches[i].lower())
		substituteEntered = input()
		substitutes.append(substituteEntered)
	else:
		print('No lines with input regex found.')