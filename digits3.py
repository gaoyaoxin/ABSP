import re

digits3Regex = re.compile(r'''^(
	\d{1,3}
	(,\d{3})*
	)$''', re.VERBOSE)
# ^ and $ are important!

text = ['42', '1,234', '6,368,745', '12,34,567' '1234']

matches = []
for i in range(len(text)):
	for groups in digits3Regex.findall(text[i]):
		digits3Found = ''.join(groups[0])
		matches.append(digits3Found)


if len(matches) > 0:
	print('Matched digits:')
	print('\n'.join(matches))
else:
	print('No digits meeting the requirement found.')
