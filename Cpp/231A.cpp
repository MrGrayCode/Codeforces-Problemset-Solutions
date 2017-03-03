/*
* Link to problem:
* http://codeforces.com/problemset/problem/231/A
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long int INT;

int main()
{
	int n;
	cin>>n;
	int a[n]={0};
	int P,V,T;
	int ans=0;
	for(int i=0;i<n;i++)
	{
		cin>>P>>V>>T;
		if(P+V+T>=2)
		{
			ans+=1;
		}
	}
	cout<<ans;
	return 0;
}
