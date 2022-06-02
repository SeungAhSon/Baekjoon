#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int x, y;
} coord;

int compare(const void* pa, const void* pb) {
    coord a = *(coord*)pa;
    coord b = *(coord*)pb;
    
    if(a.x > b.x) return 1;
    else if(a.x < b.x) return -1;
    else{
        if(a.y > b.y) return 1;
        else if(a.y < b.y) return -1;
        else return 0;
    }
}


int main() {
    int N;
    scanf("%d", &N);
    coord arr[N];
    
    for(int i=0;i<N;i++)
        scanf("%d %d",&arr[i].x, &arr[i].y);
    qsort(arr, N, sizeof(coord), compare);
    for(int i=0;i<N;i++)
        printf("%d %d\n", arr[i].x, arr[i].y);

    return 0;
}