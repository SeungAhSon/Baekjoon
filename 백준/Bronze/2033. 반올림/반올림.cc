#include <stdio.h>
int main() {
	int N, count = 0;
	scanf("%d", &N);
	while(N/10>0) {
		if(N%10>4) N=N+10;
		N=N/10;
		count++;
	}
	for(int i=0;i<count;i++) N=10*N;
	printf("%d", N);
}