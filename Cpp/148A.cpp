#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b)
{
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}

int lcm(int a,int b)
{
	return a*b/gcd(a,b);
}

int lcm(int a,int b,int c)
{
	return lcm(lcm(a,b),c);
}

int lcm(int a,int b,int c,int d)
{
	return lcm(lcm(a,b),lcm(c,d));
}


int main()
{
	int a,b,c,d,n;
	cin>>a>>b>>c>>d>>n;
	int ans=0;
	//Using theory of inclusion and exclusion
	ans+=(n/a + n/b + n/c + n/d);
	ans-=(n/lcm(a,b) + n/lcm(a,c) + n/lcm(a,d) + n/lcm(b,c) + n/lcm(b,d) + n/lcm(c,d));
	ans+=(n/lcm(a,b,c) + n/lcm(a,b,d) + n/lcm(a,c,d) + n/lcm(b,c,d));
	ans-=(n/lcm(a,b,c,d));
	cout<<ans;
	return 0;
}
