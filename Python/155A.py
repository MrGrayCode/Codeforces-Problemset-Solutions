n = int(input())
a = list(map(int,input().split()))
min_so_far = max_so_far = a[0]

num_amazing = 0

for i in range(1,n):
    if a[i] > max_so_far:
        num_amazing += 1
        max_so_far = a[i]
    elif a[i] < min_so_far:
        num_amazing += 1
        min_so_far = a[i]

print(num_amazing)