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

double covariance(double *arr1, double *arr2, size_t n) {
    double *arr1_times_arr2 = multiply_arrs(arr1, arr2, n);
    return mean(arr1_times_arr2, n) - (mean(arr1, n) * mean(arr2, n));
}

double median(double *arr, size_t n) {
    quick_sort(arr, 0, n - 1);
    if (n % 2 == 0) {
        double middle_values[2] = {arr[n/2-1], arr[n/2]};
        return mean(middle_values, 2);
    }
    return arr[(n-1)/2];
}