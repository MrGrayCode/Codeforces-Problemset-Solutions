def check(n):
	n=list(str(n))
	if n[0]!=n[1] and n[0]!=n[2] and n[0]!=n[3] and n[1]!=n[2] and n[1]!=n[3] and n[2]!=n[3]:
		return True
	else:
		return False
n=int(input())
while True:
	n+=1
	if(check(n)):
		break
print(n)
	
