#include <stdio.h>
#include <string.h>

int max(int a, int b) {  return a > b ? a : b;}

int main() {
    char num[3][9];
    int i, j, max_length;
    for (i = 0; i < 3; ++i) {  scanf("%s", num[i]);   }
    for (i = 0; i < 3; ++i) {
        int length = 1;
        max_length = 1;

        for (j = 1; j < strlen(num[i]); ++j) {
            if (num[i][j] == num[i][j - 1]) {
                length++;
            } else {
                max_length = max(max_length, length);
                length = 1;
            }
        }
        max_length = max(max_length, length);
        printf("%d\n", max_length);
    }

    return 0;
}