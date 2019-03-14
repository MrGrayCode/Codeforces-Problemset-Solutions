n = int(input())
a = list(map(int,input().split()))
max_welfare = max(a)
s = 0
for i in a:
    s += (max_welfare - i)
print(s)