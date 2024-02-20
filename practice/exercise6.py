str1 = "Venkatapathi"
str2 = "Chekuri"

len_str1 = len(str1)
len_str2 = len(str2)
extra = ""
if len_str1 < len_str2:
	length = len_str1
	s1 = str1[::]
	s2 = str2[:length+1:-1]
	extra = str2[length:]
elif len_str1 > len_str2:
	length = len_str2
	s1 = str1[:length+1]
	s2 = str2[::-1]
	extra = str1[length:]
else:
	length = len(str1)
	s1 = str1[::]
	s2 = str2[::-1]

s3 = ""
for i in range(length):
	s3 = s3+s1[i]+s2[i]

print(s3+extra)