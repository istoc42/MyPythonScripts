import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'valencia', 'st.']

# Check if cmd line args were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'valencia', 'st.'] -> '870 valencia st.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
