#include <stdio.h>
#include <stdlib.h> 

int compare(const void *a, const void *b){
    int num1 = *(int *)a;
    int num2 = *(int *)b; 

    if (num1 < num2) return 1;
    if (num1 > num2) return -1;
    return 0;
}

int main(){
	int N,count=0;
	int list[10];
	scanf("%d", &N);

	while (N > 0){
		list[count] = N%10;
		N /= 10;
		count+=1;
	}
	qsort(list, count, sizeof(int),compare);
	for(int j=0;j<count;j++) printf("%d",list[j]);
	return 0;
}