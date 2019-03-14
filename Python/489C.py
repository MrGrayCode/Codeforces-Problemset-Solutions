m, s = map(int,input().split())
if s > int(9*m):
    res = "-1 -1"
elif s == 0:
    if m == 1:
        res = "0 0"
    else:
        res = "-1 -1"
else:
    small = [0] * m
    s_temp = s
    for i in range(m-1,-1,-1):
        x = min(9,s)
        if x == 0:
            j = i+1
            while not small[j]:
                j+=1
            small[j] -= 1
            s += 1
            x = 1
        small[i] = x
        s -= x
    small = list(map(str,small))
    small = ''.join(small)

    big = [0] * m
    i = 0
    s = s_temp
    while s:
        x = min(9,s)
        big[i] = x
        s -= x
        i += 1
    big = list(map(str,big))
    big = ''.join(big)


    res = ' '.join([small,big])

print(res)

