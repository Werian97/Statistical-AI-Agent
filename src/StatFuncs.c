#include <stdio.h>
#include <math.h>

#include "utility_functions.h"

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

double min(double *arr, size_t n) {
    double min_so_far = INFINITY;
    for (size_t i = 0; i < n; i++) {
        if (*(arr+i) < min_so_far) {
            min_so_far = *(arr+i);
        }
    }
    return min_so_far;
}

double variance(double *arr, size_t n) {
    double *squared_arr = square_arr(arr, n);
    return mean(squared_arr, n) - (mean(arr, n) * mean(arr, n));
}