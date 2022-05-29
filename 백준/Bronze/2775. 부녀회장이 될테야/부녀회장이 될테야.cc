#include <stdio.h>
 
int main(){
  int A[15][15] = {0,};
  int input, h,w;

  for(int i=0; i<15; i++) A[0][i] = i;
  
  for(int i=1; i<15; i++){
    for(int j=1; j<15; j++){
      A[i][j] = A[i-1][j] + A[i][j-1];
    }
  }

  scanf("%d",&input); 
  
  for(int i=0;i<input;i++){
    scanf("%d %d", &h, &w);  
    printf("%d\n", A[h][w]);  
  }
  
	return 0; 
}