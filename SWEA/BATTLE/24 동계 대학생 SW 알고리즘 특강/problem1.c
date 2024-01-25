#include <stdio.h>
#define max(x, y) ((x) > (y) ? (x) : (y))

int calculate_min_coins(int s, int e) {
    int start_level = 0, end_level = 0, start_index, end_index, diff_index, diff_level;
    
    while ((start_level * (start_level + 1)) / 2 < s) {start_level++;}
    while ((end_level * (end_level + 1)) / 2 < e) {end_level++;}
    
    start_index = (start_level * (start_level + 1)) / 2 - s;
    end_index = (end_level * (end_level + 1)) / 2 - e;
    diff_level = start_level - end_level;
    diff_index = start_index - end_index;
    
    if (diff_level<=0 && diff_index<=0){return max(abs(diff_index),abs(diff_level));}
    else {return abs(diff_index)+abs(diff_level);}
}
int main() {
    int i, T, s, e, result, temp;
    scanf("%d", &T);

    for (i = 1; i <= T; i++) {
        scanf("%d %d", &s, &e);
        if (e<s){
          temp=s;
          s = e;
          e = temp;
        }
        
  
        int cost = calculate_min_coins(s, e);
        printf("#%d %d\n", i, cost);
    }

    return 0;
}
