#include <stdio.h>
#include <stdlib.h>
#define min(X,Y) ((X) < (Y) ? (X) : (Y))  
char chess_1[8][8] = {{ "WBWBWBWB" },{ "BWBWBWBW" },{ "WBWBWBWB" },{ "BWBWBWBW" },
                      { "WBWBWBWB" },{ "BWBWBWBW" },{ "WBWBWBWB" },{ "BWBWBWBW" }};

char chess_2[8][8] = {{ "BWBWBWBW" },{ "WBWBWBWB" },{ "BWBWBWBW" },{ "WBWBWBWB" },
                      { "BWBWBWBW" },{ "WBWBWBWB" },{ "BWBWBWBW" },{ "WBWBWBWB" }};
 


int main() {
    int N,M; scanf("%d %d",&N,&M);
    char wrongchess[55][55];
	getchar();
	
	int count_1=0,count_2=0;
	
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			scanf("%c",&wrongchess[i][j]);
		}
		getchar();
	}
	int save = 64;
	for(int i=0;i<N-7;i++){
		for(int j=0;j<M-7;j++){
			int count_1=0,count_2=0;
			for(int z=i;z<i+8;z++){
				for(int k=j;k<j+8;k++){
					if(wrongchess[z][k]!=chess_1[z-i][k-j]) count_1++;
					if(wrongchess[z][k]!=chess_2[z-i][k-j]) count_2++;
				}
			}
			save = min(save,min(count_1,count_2));
		}
	}
	printf("%d",save);
	return 0;
}