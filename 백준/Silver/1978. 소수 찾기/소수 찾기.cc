#include <stdio.h>

int main(void){
    int n;
    int temp, count=0;

    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d",&temp);
        for(int j=2;j<=temp;j++){
            if(temp==j) count++;
            if(temp%j==0) break;
        }
    }
    printf("%d", count);
    return 0;
}