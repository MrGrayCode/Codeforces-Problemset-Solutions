from math import ceil,floor,log2
ans=['Sheldon','Leonard','Penny', 'Rajesh', 'Howard']
n=int(input())
k=floor(log2((n+4)/5))
turn=n-(5*(2**k-1))
print(ans[ceil(turn/2**k)-1])
