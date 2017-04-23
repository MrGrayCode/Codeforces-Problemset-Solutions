n=int(input())
s_i=input()
ans=1
for i in range(1,n):
	s_j=input()
	if s_i!=s_j:
		ans+=1
	s_i=s_j
print(ans)
