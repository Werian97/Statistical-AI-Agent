#include <stdio.h>

int mysum(int a, int b) {
    return a+b;
}

double mean(double *arr, size_t n) {
    float tot = 0;
    for (size_t i = 0; i < n; i++) {
        tot += *(arr+i);
    }
    return tot/n;
}