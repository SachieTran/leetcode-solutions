import re

pattern = r'(((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]))\.){3}(((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]))){1}'

input = '22.233.23.100'
match = re.match(pattern,input)
if match:
	print match.group()
else:
	print "invalid"