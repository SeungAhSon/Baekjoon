#include <stdio.h>

int main() {
    int N, x=1, cnt=1;
    scanf("%d", &N);
    
    if(N==1) printf("%d", 1);
    else {
        while(1){
            if(N<=x) break;
            N-=x;
            x = cnt*6;
            cnt++;
        }
        printf("%d", cnt);
    }
    return 0;
}