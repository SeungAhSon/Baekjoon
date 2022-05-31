#include <stdio.h>

int main() {
    int N, count;
    int body[50][2];
    
    scanf("%d", &N);
    
    for(int i=0; i<N; i++)
        scanf("%d %d", &body[i][0], &body[i][1]);

    for(int i=0; i<N; i++){
        count=1;
        for(int j=0;j<N;j++){
            if(body[i][0]<body[j][0] && body[i][1]<body[j][1])
                count++;
        }
        printf("%d ", count);
    }
    return 0;
}