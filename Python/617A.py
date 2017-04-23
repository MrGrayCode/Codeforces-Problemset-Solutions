n=int(input())
steps=0
for i in range(5,0,-1):
	if n>=i:
		steps+=n//i
		n%=i
print(max(1,steps))
