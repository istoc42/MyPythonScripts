#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'([0]|\+44)(\d\d\d\d\d\d\d\d\d\d)|([0])(\d\d\d\d\d\d\d\d\d\d)')

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # username
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # domain name
    (\.[a-zA-Z]{2,4})    # dot-something
    )''', re.VERBOSE) # Use re.VERBOSE to ignore whitespace between new lines.

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ''.join([groups[0], groups[1]])
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
