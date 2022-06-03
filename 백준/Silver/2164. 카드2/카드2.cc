#include <stdio.h>
#define MAX 500001
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
    int N;
    scanf("%d", &N);
    if(N==1) {printf("1"); return 0;}
    
    for(int i=0;i<N;i++) addq(i+1,N);
    
    while(1){
        deleteq(N);
        if(front==rear) break;
        addq(deleteq(N),N);
    }
    
    printf("%d",queue[rear]);
    return 0;
}
