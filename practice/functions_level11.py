#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def capitalize_letters(name):
	if len(name) > 3:
		return name[:3].capitalize() + name[3:].capitalize()
	else:
		return (name + ' is too short for action')

print(capitalize_letters('oldmacdonald'))
print(capitalize_letters('macintyre'))
print(capitalize_letters('fox'))
