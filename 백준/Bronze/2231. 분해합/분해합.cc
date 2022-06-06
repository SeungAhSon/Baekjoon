#include <stdio.h>

int main(){
	int N;
	scanf("%d", &N);

	for (int i = 1; i < N; i++){
		int temp = i;
		int num = i;

		while (temp > 0){
			num += temp % 10;
			temp /= 10;
		}
		if (num == N){
			printf("%d", i);
			return 0;
		}
	}
	printf("0");
	return 0;
}