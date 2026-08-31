#include <stdio.h>
#include <stdlib.h>

double *square_arr(double *arr, size_t n) {
    double *new_arr = malloc(n * sizeof(double));
    for (size_t i = 0; i < n; i++) {
        *(new_arr + i) = (*(arr + i)) * (*(arr + i));
    }
    return new_arr;
}