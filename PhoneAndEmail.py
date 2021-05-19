#!python3
import re
import pyperclip
phoneregex = re.compile(r'''
((d\d\d)? #area code
(\s | -)?
(\d\d\d\d\d\d\d))''', re.VERBOSE)

emailregex = re.compile(r'''
#some.+_Thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''' ,re.VERBOSE)

text = pyperclip.paste()
phonextracted = phoneregex.findall(text)
emailextracted = emailregex.findall(text)

allphonenumber = []

for phonenumber in phonextracted:
    allphonenumber.append(phonenumber[0])

result ='\n'.join(allphonenumber) + '\n' + '\n'.join(emailextracted)
pyperclip.copy(result)
