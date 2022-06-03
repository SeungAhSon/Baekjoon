#include <stdio.h>

int main(){
    int N, M, temp, result=0;
    scanf("%d %d", &N, &M);
    
    int card[N];
    for(int i=0;i<N;i++) scanf("%d", &card[i]);

	for (int i = 0; i < N - 2; i++) {
		for (int j = i + 1; j < N - 1; j++) {
		    for (int k = j + 1; k < N; k++) {
				temp = card[i] + card[j] + card[k];
				if(result < temp && temp <= M) result = temp;
			}
		}
	}
	printf("%d", result);
	return 0;
}