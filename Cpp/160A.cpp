#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	vector<int> a(n);
	int sum=0;
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		sum+=a[i];
	}
	sort(a.rbegin(),a.rend());
	int count=0,sum_till_now=0;
	for(int i=0;i<n;i++)
	{
		sum_till_now+=a[i];
		count++;
		if(sum_till_now>sum-sum_till_now)
		{
			break;
		}
	}
	cout<<count;
	return 0;
}
