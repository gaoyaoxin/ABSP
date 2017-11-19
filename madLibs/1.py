#! python3
# madLibs.py - A Mad Libs game, loading a sample text, asking for inputs and outputing a result text.

import re

# Open a text.
print("Please input a .txt file's name, without extension. For instance, sample")
originalFileName = input()
originalFile = open('%s.txt' % (originalFileName))
text = originalFile.read()


# Find UPPERCASE words.
uppercaseRegex = re.compile(r'''(
	[A-Z]{2,} # Only one uppercase letter may be the first letter of first word in a sentence.
	)''', re.VERBOSE)

matches = []
for groups in uppercaseRegex.findall(text):
	uppercaseFound = ''.join(groups[0])
	matches.append(uppercaseFound)


# Ask for inputs.
substitutes = []
if len(matches) > 0:
	for i in range(len(matches)):
		# this need to be fixed. print('Enter a/an %s:' % (matches[i].lower()))
		print('Enter a/an' + matches[i].lower())
		substituteEntered = input()
		substitutes.append(substituteEntered)
else:
	print('No uppercase words found.')

# TODO: Use substitutes to substitute matches!

# Print result.
# Save result in a .txt file.


