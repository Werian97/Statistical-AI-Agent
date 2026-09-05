#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include "utility_functions.h"

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
    double result = mean(squared_arr, n) - (mean(arr, n) * mean(arr, n));
    free(squared_arr);
    return result;
}

double covariance(double *arr1, double *arr2, size_t n) {
    double *arr1_times_arr2 = multiply_arrs(arr1, arr2, n);
    double result = mean(arr1_times_arr2, n) - (mean(arr1, n) * mean(arr2, n));
    free(arr1_times_arr2);
    return result;
}

double median(double *arr, size_t n) {
    quick_sort(arr, 0, n - 1);
    if (n % 2 == 0) {
        double middle_values[2] = {arr[n/2-1], arr[n/2]};
        return mean(middle_values, 2);
    }
    return arr[(n-1)/2];
}

char *mode(char **arr, size_t n) {
    /*If there are 2 or more values with the same occurrancy number
    this function will return the (alphabetical) biggest string*/
    quick_sort_string(arr, 0, n-1);
    size_t current_winner_occurrency = 0;
    size_t contendent_occurrency = 0;
    char *current_winner = arr[0];
    char *contendent = arr[0];
    for (size_t i = 0; i < n; i++) {
        if (strcmp(contendent, arr[i]) != 0) {
            contendent = arr[i];
            contendent_occurrency = 0;
        }
        if (strcmp(current_winner, contendent) == 0) {
            current_winner_occurrency++;
        } else {
            contendent_occurrency++;
        }
        if (contendent_occurrency > current_winner_occurrency) {
            current_winner = contendent;
            current_winner_occurrency = contendent_occurrency;
        }
    }
    return current_winner;
}
