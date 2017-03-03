#include<bits/stdc++.h>
using namespace std;
typedef long long int INT;
int main()
{
	double n,m,a;
	cin>>n>>m>>a;
	INT ans=ceil(n/a)*ceil(m/a);
	cout<<ans;
	return 0;
}
