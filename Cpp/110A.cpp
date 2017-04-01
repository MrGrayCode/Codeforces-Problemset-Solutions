#include<bits/stdc++.h>
using namespace std;

bool lucky(int n)
{
	while(n>0)
	{
		if(n%10!=4 && n%10!=7)
		{
			return false;
		}
		n/=10;
	}
	return true;
}

int main()
{	
	string n;
	cin>>n;
	int count=0;
	int len=n.length();
	for(int i=0;i<len;i++)
	{
		if(n[i]=='4' || n[i]=='7')
		{
			count++;
		}
	}
	if(count>0 && lucky(count))
	{
		cout<<"YES";
	}
	else
	{
		cout<<"NO";
	}
return 0;
}
