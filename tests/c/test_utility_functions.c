#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#include "utility_functions.h"

int main() {
    double arr1[5] = {5.0, 4.0, 3.0, 2.0, 1.0};
    quick_sort(arr1, 0, 4);
    assert(arr1[0] == 1.0);
    assert(arr1[1] == 2.0);
    assert(arr1[2] == 3.0);
    assert(arr1[3] == 4.0);
    assert(arr1[4] == 5.0);

    double arr2[5] = {3.0, 3.0, 2.0, 2.0, 4.0};
    quick_sort(arr2, 0, 4);
    assert(arr2[0] == 2.0);
    assert(arr2[1] == 2.0);
    assert(arr2[2] == 3.0);
    assert(arr2[3] == 3.0);
    assert(arr2[4] == 4.0);

    double *arr3 = square_arr(arr1, 5);
    assert(arr3[0] == 1.0);
    assert(arr3[1] == 4.0);
    assert(arr3[2] == 9.0);
    assert(arr3[3] == 16.0);
    assert(arr3[4] == 25.0);

    double *arr4 = multiply_arrs(arr1, arr2, 5);
    assert(arr4[0] == 2.0);
    assert(arr4[1] == 4.0);
    assert(arr4[2] == 9.0);
    assert(arr4[3] == 12.0);
    assert(arr4[4] == 20.0);

    char first_str[5] = "ciao";
    char second_str[6] = "prova";
    char third_str[4] = "zzz";
    char *arr_str[3] = {
        second_str,
        third_str,
        first_str,
    };
    quick_sort_string(arr_str, 0, 2);
    assert(strcmp(arr_str[0], "ciao") == 0);
    assert(strcmp(arr_str[1], "prova") == 0);
    assert(strcmp(arr_str[2], "zzz") == 0);

    printf("Every test for utility functions in C was successful\n");

    return 0;
}