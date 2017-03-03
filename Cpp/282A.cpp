/*
* Link for the problem statement
* http://codeforces.com/problemset/problem/282/A
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long int INT;

int main()
{
	int n;
	cin>>n;
	string s;
	int ans=0;
	while(n--)
	{
		cin>>s;
		switch(s[1])
		{
			case '+': ans++;
					  break;
			case '-': ans--;
					  break;
		}
	}
	cout<<ans;
	return 0;
}
