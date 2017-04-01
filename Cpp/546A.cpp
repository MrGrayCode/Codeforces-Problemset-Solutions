#include<bits/stdc++.h>
using namespace std;

int main()
{
	int k,n,w;
	cin>>k>>n>>w;
	int required=(k*w*(w+1))/2;
	int res=max(0,required-n);
	cout<<res;
	return 0;
}
