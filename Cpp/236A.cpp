#include<bits/stdc++.h>
using namespace std;

int main()
{
	string s;
	cin>>s;
	bool alpha[26]={false};
	int n=s.length();
	int count=0;
	for(int i=0;i<n;i++)
	{
		if(alpha[s[i]-'a']==false)
		{
			count++;
			alpha[s[i]-'a']=true;
		}
	}
	if(count%2==0)
	{
		cout<<"CHAT WITH HER!";
	}
	else
	{
		cout<<"IGNORE HIM!";
	}
	return 0;
}
