s=input()
count_lower=count_upper=0
for i in s:
	if i.islower():
		count_lower+=1
	else:
		count_upper+=1
if count_lower>=count_upper:
	print(s.lower())
else:
	print(s.upper())
