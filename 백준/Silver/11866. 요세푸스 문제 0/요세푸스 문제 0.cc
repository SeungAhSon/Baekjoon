#include <stdio.h>
#define MAX 1001
int front=-1;
int rear=-1;
int queue[MAX];
 
void addq(int value, int N){
    rear = (rear+1)%N;
    queue[rear]=value;
}

int deleteq(int N){
    front = (front+1)%N;
    return queue[front];
}
 
int main(){
    int N, K;
    scanf("%d %d", &N, &K);
    
    for(int i=0;i<N;i++) addq(i+1,N);
    
    int count = 0, temp;
    printf("<");
    for(int i=0;i<N-1;i++){
        for(int j=0;j<K-1;j++){
            temp = deleteq(N);
            addq(temp,N);
        }
        temp = deleteq(N);
        printf("%d, ",temp);
    }
    printf("%d>",queue[rear]);
    return 0;
}
