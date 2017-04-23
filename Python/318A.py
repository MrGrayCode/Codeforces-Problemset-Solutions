from math import ceil
n,k=map(int,input().split())
i=ceil(n/2)
if k<=i:
	print(2*k-1)
else:
	print(2*(k-i))

