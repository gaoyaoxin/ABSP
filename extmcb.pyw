#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe extmcb.pyw save <keyword> ------ Saves clipboard to keyword.
#        py.exe extmcb.pyw <keyword> ----------- Loads keyword to clipboard.
#        py.exe extmcb.pyw list ----------- Loads all keywords to clipboard.
#        py.exe extmcb.pyw delete <keyword> - Delete keyword from clipboard.
#        py.exe extmcb.pyw delete ------ Delete all keywords from clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('extmcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()

if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': #########extended features!!!!!!!!!!1
	del mcbShelf.keys(sys.argv[2])###########extended features!!!!!!!!!!1

elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'delete':#######extended features!!!!!!!!!!1
		del mcbShelf.keys()########extended features!!!!!!!!!!1

	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()