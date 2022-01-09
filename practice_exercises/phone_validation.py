import re
''''
Check if phone starts with 1, 8 or 9 and is length 8.
'''

pattern = r"[/A189][0-9]"
phone = '89234567'

if re.match(pattern, phone):
  if len(phone) == 8:
    print("Valid")
  else:
    print("Invalid")
else:
    print("Invalid")
