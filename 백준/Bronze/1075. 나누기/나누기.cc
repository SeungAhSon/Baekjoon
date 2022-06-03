#include <stdio.h>

int main() {
    int N,F,i;
    scanf("%d %d",&N,&F);
    N = (N/100)*100;
    
    for(i=0;i<100;i++){
        if((N+i)%F==0) {
            printf("%02d",i);
            return 0;
        }
    }
    printf("%02d",i);
    return 0;
}