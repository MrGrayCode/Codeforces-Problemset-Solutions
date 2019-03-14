n,m,a,b = map(int,input().split())
if a*m > b:
    res = b*(n//m)
    rem = n%m
    if a*rem > b:
        res += b
    else:
        res += a*rem
else:
    res = a*n
print(res)