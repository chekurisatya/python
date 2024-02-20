#str1 = "P@#yn26at^&i5ve"
str1 = "helo%(*^)234&&%%asdjklaksdlfhlakdf&&^&#(&^1215236345124124#((#(@&#@&##))))asdfasd"

char = digit = symbol = 0

for m in str1:
	if m.isalpha():
		char += 1
	elif m.isdigit():
		digit += 1
	else:
		symbol += 1

print ("Chars =", char)
print ("Digits =", digit)
print ("Symbol =", symbol)