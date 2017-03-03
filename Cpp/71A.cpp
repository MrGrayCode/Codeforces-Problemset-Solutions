/*
* Link for the problem statement
* http://codeforces.com/problemset/problem/71/A
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long int INT;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		int n=s.length();
		if(n<=10)
		{
			cout<<s<<"\n";
		}
		else
		{
			cout<<s[0]<<n-2<<s[n-1]<<"\n";
		}
	}
	return 0;
}
