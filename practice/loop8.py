#Display all prime numbers with in a range

number = 100
count = 0
for j in range(3,number+1,2):
    for k in range(3,j,2):
        if j % k == 0:
        	break
    else:
        count += 1
        print(j)

print (f'Total number of primes are: {count}')