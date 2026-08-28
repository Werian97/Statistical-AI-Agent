#include <stdio.h>
#include <math.h>

int mysum(int a, int b) {
    return a+b;
}

double mean(double *arr, size_t n) {
    double tot = 0;
    for (size_t i = 0; i < n; i++) {
        tot += *(arr+i);
    }
    return tot/n;
}

double max(double *arr, size_t n) {
    double max_so_far = -1 * INFINITY;
    for (size_t i = 0; i < n; i++) {
        if (*(arr+i) > max_so_far) {
            max_so_far = *(arr+i);
        }
    }
    return max_so_far;
}