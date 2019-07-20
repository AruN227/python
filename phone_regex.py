import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                                # @ symbol
    [a-zA-Z0-9.-]+                   # domain name
    (\.[a-zA-Z]{2,4})                # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.

text = "arun@gmail.com and sk@gmail.com 043-123-7890"
matches = []
matches1 = []
for groups in phoneRegex.findall(text):   
    matches.append(groups[0])

for groups in emailRegex.findall(text):
    matches1.append(groups[0])

# Copy results to the clipboard.

print(matches1)
print(matches)