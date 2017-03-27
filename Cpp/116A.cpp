/*
Problem Link: http://codeforces.com/problemset/problem/116/A
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,a,b;
	cin>>n;
	int max_strength=0,total=0;
	for(int i=0;i<n;i++)
	{
		cin>>a>>b;
		total+=(b-a);
		max_strength=max(max_strength,total);
	}
	cout<<max_strength;
	return 0;
}
