#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char Board[50][50];

typedef struct {
    char string[51];
    int length;
} str;

str words[20001];

int compare(const void* pa, const void* pb) {
    str a = *(const str*)pa;
    str b = *(const str*)pb;
    
    if(a.length > b.length) return 1;
    else if(a.length < b.length) return -1;
    else return strcmp(a.string, b.string);
}


int main() {
    int N;
    
    scanf("%d", &N);
    str arr[N];
    
    for(int i=0;i<N;i++){
        scanf("%s",arr[i].string);
        arr[i].length = strlen(arr[i].string);

    }
    qsort(arr, N, sizeof(str), compare);
    
    printf("%s\n", arr[0].string);
    for(int i=1;i<N;i++){
        if(strcmp(arr[i-1].string, arr[i].string)!=0)  printf("%s\n", arr[i].string);
    }
    return 0;
}