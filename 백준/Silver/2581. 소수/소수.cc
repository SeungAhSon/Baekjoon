#include <stdio.h>

int main() {
    int M,N;
    scanf("%d %d", &M, &N);
    int flag, sum=0, min=0;
    
    for(int i=M;i<=N;i++){
        flag=0;
        if(i==1) continue;
        else{
            for(int j=2;j<i;j++)
                if(i%j==0) flag=1;
            if(flag==0){
                if(sum==0) min=i;
                sum+=i;
            }
        }
    }
    if(sum==0) printf("%d",-1);
    else printf("%d\n%d\n", sum, min);
    
    return 0;
}