n=int(input())
a=[]
for i in range(n):
	x=list(map(int,input().split()))
	a.append(x)
ans=0
for i in range(n):
	for j in range(n):
		if j!=i and a[i][0]==a[j][1]:
			ans+=1
print(ans)
