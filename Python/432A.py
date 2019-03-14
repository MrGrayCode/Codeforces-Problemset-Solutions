n, k = map(int,input().split())
a = list(map(int,input().split()))
count = 0
k = 5-k
for i in a:
    if i <= k:
        count += 1
res = count//3
print(res)