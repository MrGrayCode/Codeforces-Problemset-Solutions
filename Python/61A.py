s1=input()
s2=input()
ans=''
l=len(s1)
for i in range(l):
	if s1[i]==s2[i]:
		ans+='0'
	else:
		ans+='1'
print(ans)
