n = int(input())
a = list(map(int,input().split()))
num_crimes_untreated = 0
num_police_available = 0
for i in a:
    if i == -1:
        if num_police_available == 0:
            num_crimes_untreated += 1
        else:
            num_police_available -= 1
    else:
        num_police_available += i
print(num_crimes_untreated)