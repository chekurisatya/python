numbers = [12, 75, 150, 180, 145, 525, 50]

for j in numbers:
	if j > 500:
		break
	elif j > 150:
		continue
	elif j % 5 == 0:
		print(j)



