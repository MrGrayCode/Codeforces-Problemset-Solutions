#include<bits/stdc++.h>
using namespace std;

#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)

int main()
{	
	int s,n;
	cin>>s>>n;
	vector< pair<int,int> > a;
	for(int i=0;i<n;i++)
	{
		int x,y;
		cin>>x>>y;
		a.push_back(mp(x,y));
	}
	sort(a.begin(),a.end());
	string ans="YES";
	for(int i=0;i<n;i++)
	{
		if(a[i].first>=s)
		{
			ans="NO";
			break;
		}
		else
		{
			s+=a[i].second;
		}
	}
	cout<<ans;
	return 0;
}
