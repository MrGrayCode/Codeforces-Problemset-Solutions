/*
* Link for the problem statement
* http://codeforces.com/problemset/problem/282/A
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long int INT;

int main()
{
	string s;
    cin>>s;
    string case1="0000000";
    string case2="1111111";
    if(s.find(case1)!=string::npos || s.find(case2)!=string::npos)
        {
        cout<<"YES";
    }
    else
        {
        cout<<"NO";
    }
}
