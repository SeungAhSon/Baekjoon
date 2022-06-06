#include <stdio.h>
#include <stdlib.h> 
#include <math.h>

int compare(const void *a, const void *b){
    int num1 = *(int *)a;
    int num2 = *(int *)b; 

    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

//최빈값에서 이중 반복문을 쓰면 "시간초과"
//참고 : https://sedangdang.tistory.com/19
int mode(int list[], int n){
	int ar[8001] = {0};
	int i, idx, max = 0, cnt = 0;

	for (i = 0; i < n; i++){
		ar[list[i]+4000] += 1;
		if (ar[list[i]+4000] > max) max = ar[list[i]+4000];
	}

	for (i = 0, idx = 0; i < 8001 ; i++){
		if (ar[i] == 0)	continue;

		if (ar[i] == max){
			if (cnt == 0){
				idx = i;
				cnt += 1;
			}
			else if (cnt == 1){
				idx = i;
				break;
			}
		}
	}
	return idx-4000;
}

int main(){
	int N;
	double sum=0;
	scanf("%d", &N);
    int list[N];
    
    for(int i=0;i<N;i++){
        scanf("%d", &list[i]);
        sum+=list[i];
    }
    
    if(N==1){
        printf("%d\n%d\n%d\n%d\n",list[0],list[0],list[0],0);
        return 0;
    }

	qsort(list, N, sizeof(int), compare);

	printf("%d\n",(int) round(sum/N));
	printf("%d\n",list[(int)((N+1)/2-1)]);
	printf("%d\n",mode(list,N));
	printf("%d\n", list[N-1]-list[0]);
} 