import re

nakamotoRegex = re.compile(r'''(
	[A-Z]+      # begins with an uppercase letter
	[a-zA-Z]*   # letters following in the given name
	\s          # space
	Nakamoto    # family name
	)''', re.VERBOSE)

text = '''Satoshi Nakamoto
          Alice Nakamoto
          RoboCop Nakamoto
          satoshi Nakamoto
          Mr. Nakamoto
          Nakamoto, Satoshi nakamoto'''


matches = nakamotoRegex.findall(text)


if len(matches) > 0:
	print('Matched names:')
	print('\n'.join(matches))
else:
	print('No full names with the family name of Nakamoto found.')
