'''
* Link for the problem statement
* http://codeforces.com/problemset/problem/282/A
'''

n=int(input().strip())
ans=0
for i in range(n):
	s=input()
	if s[1]=='+':
		ans+=1
	else:
		ans-=1
print(ans)
