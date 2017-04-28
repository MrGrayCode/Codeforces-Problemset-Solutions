n=int(input())
s=input().lower()
if n<26:
	ans='NO'
elif len(set(s))<26:
	ans='NO'
else:
	ans='YES'
print(ans)
