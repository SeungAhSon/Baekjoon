#include <stdio.h>

#define _USE_MATH_DEFINES
#include <math.h>

int main() {
    double R;
    scanf("%lf", &R);
    
    printf("%.6lf %.6lf", R*R*M_PI, 2*R*R);
    return 0;
}