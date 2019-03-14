k, r = map(int,input().split())
found = False
i = 0
while not found:
    i += 1
    c = i*k
    if c%10 == 0 or c%10 == r:
        found = True

print(i)