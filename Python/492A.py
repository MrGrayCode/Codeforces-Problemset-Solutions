def compute(n):
    return n*(n+1)*(n+2)

n = int(input())
res = int(pow(6*n,1/3))
while compute(res) > 6*n:
    res -= 1
print(res)