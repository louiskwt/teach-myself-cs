import re

# creating a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

match_object = phoneNumRegex.search('Contact me at 415-900-3333 now.')

print('Phone number found: ' + match_object.group())
