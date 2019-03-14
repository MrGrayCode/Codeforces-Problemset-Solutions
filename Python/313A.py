n = int(input())
res = n
if n < 0:
    n = abs(n)
    res = min(n//10,(n//100)*10+(n%10))
    res *= -1
print(res)