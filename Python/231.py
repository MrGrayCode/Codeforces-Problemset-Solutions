'''
* Link to problem:
* http://codeforces.com/problemset/problem/231/A
'''

def sum(a):
    res=0
    for i in a:
        res+=int(i)
    return res

n=int(input().strip())
ans=0
for i in range(n):
    team=input().strip().split()
    if sum(team)>=2:
        ans+=1
print(ans)
