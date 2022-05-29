#include <stdio.h>
 
int main(){
  int input,h,w,n;
  int ans1, ans2;
  scanf("%d",&input); 
  
  for(int i=0;i<input;i++){
    scanf("%d %d %d", &h, &w, &n);
    if(n%h==0){
        ans1 = h;
        ans2 = n/h;
    }else{
        ans1 = (n%h);
        ans2 = (1+n/h);
    };
    
    printf("%d%02d\n", ans1,ans2);  
  }
  return 0; 
}