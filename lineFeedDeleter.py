#! python3
# lineFeedDeleter.py - Delete line feeds of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and delete line feeds.
lines = text.split('\n') # each string in "lines" list are without line feeds already!
text = ''.join(lines)

pyperclip.copy(text)