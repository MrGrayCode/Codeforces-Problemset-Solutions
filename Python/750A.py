n,k = map(int,input().split())

times = [int(2.5*i*(i+1)) for i in range(1,n+1)]

time_left = 240 - k

beg = 0
end = n-1

while beg < end:
    mid = (beg+end)//2

    if times[mid] > time_left:
        end = mid
    elif times[mid] <= time_left:
        beg = mid + 1

if times[beg] <= time_left:
    res = beg + 1
else:
    res = beg

print(res)