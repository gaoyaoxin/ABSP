import re

aliceBobRegex = re.compile(r'''(
	(Alice|Bob|Carol)       # first word
	(\s)                      # space
	(eats|pets|throws)      # second word
	(\s)                      # space
	(apples|cats|baseballs) # third word
	(.)                      # ends with dot
	)''', re.VERBOSE | re.IGNORECASE)

text = '''Alice eats apples.
          Bob pets cats.
          Carol throws baseballs.
          Alice throws Apples.
          BOB EATS CATS.
          Robocop eats apples.
          ALICE THROWS FOOTBALLS.
          Carol eats 7 cats.'''

matches = []
for groups in aliceBobRegex.findall(text):
	sentencesFound = ''.join(groups[1:7])
	matches.append(sentencesFound)


if len(matches) > 0:
	print('Matched sentences:')
	print('\n'.join(matches))
else:
	print('No sentences meeting the requirement found.')
