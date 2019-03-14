from math import sqrt
'''
def isPrime(n):
    l = int(sqrt(n))
    for i in range(2,l+1):
        if n%i == 0:
            return False
    return True
'''

limit = 1000000
isPrime = [True for i in range(limit + 1)]
isPrime[1] = False

p = 2
while p*p <= limit:
    if isPrime[p]:
        for i in range(2*p,limit+1,p):
            isPrime[i] = False
    p += 1

def isTprime(n):
    x = int(sqrt(n))
    if x*x == n:
        return isPrime[x]
    else:
        return False

n = int(input())
a = list(map(int,input().split()))
for i in a:
    if isTprime(i):
        res = "YES"
    else:
        res = "NO"
    print(res)
