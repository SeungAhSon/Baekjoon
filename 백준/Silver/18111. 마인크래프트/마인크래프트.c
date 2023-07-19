#include <stdio.h>

int main() {
    int N, M, B;
    scanf("%d %d %d", &N, &M, &B);

    int ground[N][M];
    int minHeight = 256, maxHeight = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &ground[i][j]);
            minHeight = (ground[i][j] < minHeight) ? ground[i][j] : minHeight;
            maxHeight = (ground[i][j] > maxHeight) ? ground[i][j] : maxHeight;
        }
    }

    int minTime = 2e9;
    
    for (int height = 0; height <= 256; height++) {
        int inventory = B;
        int total_time = 0;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                int diff = ground[i][j] - height;
                if (diff<0) {
                    total_time -= diff;
                    inventory += diff;
                }else if (diff>0) {
                    total_time += 2*diff;
                    inventory += diff;
                }
            }
        }
        
        if (inventory >= 0 && total_time <= minTime) {
            minTime = total_time;
            maxHeight = height;
        }
    }

    printf("%d %d\n", minTime, maxHeight);
    return 0;
}
