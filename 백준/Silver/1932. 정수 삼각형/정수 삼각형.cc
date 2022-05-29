#include <stdio.h>
#include <algorithm>
using namespace std;

int tri[501][501];

int main(){
	int n;
	scanf("%d",&n);
	
	for(int i=0;i<n;i++)
		for(int j=0;j<i+1;j++)
			scanf("%d",&tri[i][j]);
	
	for(int i=n-1;i>=1;i--)
		for(int j=0;j<i;j++)
			tri[i-1][j] += max(tri[i][j],tri[i][j+1]);
	
	printf("%d",tri[0][0]);
	
	return 0;
}