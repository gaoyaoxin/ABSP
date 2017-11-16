import re

print('Please input a password.')
text = str(input())



strongPasswordLengthRegex = re.compile(r'''^(
	.{8,}
	)$''', re.VERBOSE)
# ^ and $ are important!

strongPasswordUpperCaseRegex = re.compile(r'''(
	[A-Z]+
	)''', re.VERBOSE)

strongPasswordLowerCaseRegex = re.compile(r'''(
	[a-z]+
	)''', re.VERBOSE)

strongPasswordDigitRegex = re.compile(r'''(
	\d+
	)''', re.VERBOSE)


len = strongPasswordLengthRegex.search(text)
upper = strongPasswordUpperCaseRegex.search(text)
lower = strongPasswordLowerCaseRegex.search(text)
digit = strongPasswordDigitRegex.search(text)


print('Is your password strong enough?')
if len and upper and lower and digit:
	print('Yes.')
else:
	print('No.')
