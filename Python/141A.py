s1=list(input())
s2=list(input())
s=list(input())
l=s1+s2
s.sort()
l.sort()
if s==l:
	ans='YES'
else:
	ans='NO'
print(ans)

