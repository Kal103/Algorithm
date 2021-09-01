/* 
author : @akash kumar 
*/


#include<bits/stdc++.h>
using namespace std;

void LongestSubarraySum()
{
	int n;
	cin>>n;
	vector<int>a(n);
	for(int i=0;i<n;++i)
	{
		cin>>a[i];
	}

	//logic 
	int ans=INT_MIN;
	int tmp_ans=0;

	for(int i=0;i<n;++i)
	{
		if(a[i]<=a[i]+tmp_ans)
		{
			tmp_ans+=a[i];
		}
		else
		{
			tmp_ans=a[i];
		}
		if(ans<tmp_ans)
		{
			ans=tmp_ans;
		}
	}
	cout<<ans;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		LongestSubarraySum();
		cout<<"\n";
	}
	return 0;
}
