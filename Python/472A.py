from math import sqrt,ceil,floor

def isPrime(n):
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i+=1
	return True
		

n=int(input())
a=ceil(n/2)
b=floor(n/2)
while isPrime(a) or isPrime(b):
	a+=1
	b-=1
print(a,b)
	
