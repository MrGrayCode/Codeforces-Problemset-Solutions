'''
* Link for the problem statement
* http://codeforces.com/problemset/problem/1/A
'''

import math
n,m,a=map(float,input().strip().split())
ans=math.ceil(n/a)*math.ceil(m/a)
print(int(ans))
