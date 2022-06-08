#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main(void){
    int arr[500001], N, M;
    scanf("%d",&N);
    for(int i=0;i<N;i++) scanf("%d",&arr[i]);
    sort(arr,arr+N);
    scanf("%d",&M);
    for (int i=0;i<M;i++){
        int target;
        scanf("%d",&target);
        int left=0,right=N-1,mid;
        while(left<=right){
            mid = (left+right)/2;
            if(target>arr[mid]) left = mid+1;
            else if(target<arr[mid]) right = mid-1;
            else break;
        }
        if (left<=right) printf("1 ");
        else printf("0 ");
    }
}