n=int(input())
a=list(map(int,input().split()))
MIN=MAX=a[0]
MIN_pos=MAX_pos=0
for i in range(n):
	if a[i]<=MIN:
		MIN=a[i]
		MIN_pos=i
	elif a[i]>MAX:
		MAX=a[i]
		MAX_pos=i
ans=(MAX_pos)+(n-1-MIN_pos)
if MIN_pos<MAX_pos:
	ans-=1
print(ans)
