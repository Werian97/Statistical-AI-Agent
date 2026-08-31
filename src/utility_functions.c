#include <stdio.h>
#include <stdlib.h>

double *square_arr(double *arr, size_t n) {
    double *new_arr = malloc(n * sizeof(double));
    for (size_t i = 0; i < n; i++) {
        *(new_arr + i) = (*(arr + i)) * (*(arr + i));
    }
    return new_arr;
}

double *multiply_arrs(double *arr1, double *arr2, size_t n) {
    double *new_arr = malloc(n * sizeof(double));
    for (size_t i = 0; i < n; i++) {
        *(new_arr + i) = (*(arr1 + i)) * (*(arr2 + i));
    }
    return new_arr;
}


void myswap(double *arr, int i, int j) {
    double temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    return;
}

void quick_sort(double *arr, int first, int last) {
    if (last - first <= 0) {
        return;
    }

    int pivot_index = last;
    double pivot = *(arr + pivot_index);
    int i = first - 1;
    for (int j = first; j < last; j++) {
        if (arr[j] < pivot) {
            i++;
            myswap(arr, i, j);
        }
    }
    myswap(arr, ++i, pivot_index); // now i is the pivot index
    quick_sort(arr, first, i - 1);
    quick_sort(arr, i + 1, last);
    return;
}