n,m=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
ans=a[m-1]-a[0]
for i in range(m-n+1):
	ans=min(ans,a[i+n-1]-a[i])
print(ans)
