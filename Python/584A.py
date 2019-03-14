n, t = map(int,input().split())
if t < 10:
    t = str(t)
    res = t*n
else:
    if n == 1:
        res = -1
    else:
        res = 10**(n-1)
print(res)