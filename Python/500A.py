n,t=map(int,input().split())
a=list(map(int,input().split()))
a.append(1)
i=0
ans='NO'
while i<n:
	if (i+1)==t:
		ans='YES'
		break
	else:
		i+=a[i]
print(ans)
