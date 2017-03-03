'''
* Link for the problem statement
* http://codeforces.com/problemset/problem/118/A
'''
s=input().strip()
s=s.lower()
vowels='aeiouy'
for i in s:
    if i not in vowels:
        print('.'+i,end='')
