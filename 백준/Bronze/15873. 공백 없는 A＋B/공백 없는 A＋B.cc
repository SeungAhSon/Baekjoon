#include <stdio.h>

int main(void){
    int a;
    scanf("%d",&a);

    if(100>a) printf("%d",a/10+a%10);
    else if(a%10==0) printf("%d",a/100+10);
    else printf("%d",a%100+10);

    return 0;
}