n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=l[0]-1
for i in range(1,m):
	ans+=((n-l[i-1])+l[i])%n
print(ans)
