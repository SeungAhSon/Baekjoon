#include <stdio.h>

void fibonacci(int num) {
    int a=0,b=1,result=0;
    for(int i=0;i<=num;i++){
        a = b;
        b = result;
        result = a+b;
    }
    
    printf("%d %d\n",a,b);
}
int main(){
    int N, num;
	scanf("%d",&N);
	for(int i=0;i<N;i++){
		scanf("%d",&num);
		if(num==0) printf("1 0\n");
		else if(num==1) printf("0 1\n");
		else{
			fibonacci(num);
		}
	}
	return 0;
}