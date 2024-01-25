#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generate_combinations(int n, int r, int combinations[][3], int* comb_count) {
    *comb_count = 0;
    int chosen[3] = {0};

    for (int i = 0; i < n - 2; i++) {
        chosen[0] = i;
        for (int j = i + 1; j < n - 1; j++) {
            chosen[1] = j;
            for (int k = j + 1; k < n; k++) {
                chosen[2] = k;
                memcpy(combinations[(*comb_count)++], chosen, 3 * sizeof(int));
            }
        }
    }
}


int main() {
    int T, n, i;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);

        if (n < 3) {
            for (i = 0; i < n; i++) {
                int dummy;
                scanf("%d %d %d", &dummy, &dummy, &dummy);
            }
            printf("#%d -1\n", t);
        } else {
            int rows_sum = 0, entire_rows_max_value = 0, comb_count;
            int entire_rows[50][3];// MAX_ROWS=50
            int combinations[19600][3];// MAX_COMBINATIONS=19600

            for (i = 0; i < n; i++) {
                scanf("%d %d %d", &entire_rows[i][0], &entire_rows[i][1], &entire_rows[i][2]);
                rows_sum += entire_rows[i][0] + entire_rows[i][1] + entire_rows[i][2];
            }

            int row_max[50];
            for (i = 0; i < n; i++) {
                row_max[i] = entire_rows[i][0];
                for (int j = 1; j < 3; j++) {
                    if (entire_rows[i][j] > row_max[i]) {  row_max[i] = entire_rows[i][j];  }
                }
            }

            generate_combinations(n, 3, combinations, &comb_count);

            for (i = 0; i < comb_count; i++) {
                int combination_max = 0;
                for (int z = 0; z < 3; z++) {
                    for (int j = 0; j < 3; j++) {
                        if (j != z) {
                            for (int k = 0; k < 3; k++) {
                                if (k != z && k != j) {
                                    int sum = entire_rows[combinations[i][0]][z] + entire_rows[combinations[i][1]][j] + entire_rows[combinations[i][2]][k];
                                    if (sum > combination_max) {  combination_max = sum;  }
                                }
                            }
                        }
                    }
                }
                
                
                
                int remaining_max = 0;
                for (int row = 0; row < n; row++) {
                    int is_selected = 0;
                    for (int j = 0; j < 3; j++) {
                        if (combinations[i][j] == row) {
                            is_selected = 1;
                            break;
                        }
                    }
                    if (!is_selected) {  remaining_max += row_max[row];  }
                }
                
                int temp = combination_max + remaining_max;
                if (temp > entire_rows_max_value) {  entire_rows_max_value = temp;  }
            }

            int ans = rows_sum - entire_rows_max_value;
            printf("#%d %d\n", t, ans);
        }
    }

    return 0;
}
