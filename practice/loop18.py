#Print the following pattern

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

sym = '*'
top = 5
start = 1

while start <= top:
	print (start*sym)
	start+=1

while top > 0:
	top -= 1
	print(top*sym)
