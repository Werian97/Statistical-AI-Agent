#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <StatFuncs.h>
#include <string.h>

int main() {
    double arr1[] = {2.0, -2.0};
    double arr2[] = {20.0, 13.0, -3.0};
    double arr3[] = {-5.0, 10.0, 7.0};

    assert(abs(0.0 - mean(arr1, 2)) < 1e-6);
    assert(abs(10.0 - mean(arr2, 3)) < 1e-6);
    assert(abs(4.0 - mean(arr3, 3)) < 1e-6);

    assert(max(arr1, 2) == 2.0);
    assert(max(arr2, 3) == 20.0);
    assert(max(arr3, 3) == 10.0);

    assert(min(arr1, 2) == -2.0);
    assert(min(arr2, 3) == -3.0);
    assert(min(arr3, 3) == -5.0);

    assert(abs(variance(arr1, 2) - 4.0) < 1e-6);
    assert(abs(variance(arr2, 3) - 92.6666666) < 1e-6);
    assert(abs(variance(arr3, 3) - 42.0) < 1e-6);

    assert(abs(covariance(arr1, arr1, 2) - 4.0) < 1e-6);
    assert(abs(covariance(arr2, arr3, 3) + 37.0) < 1e-6);

    assert(median(arr1, 2) == 0.0);
    assert(median(arr2, 3) == 13.0);
    assert(median(arr3, 3) == 7.0);

    char *arr_str1[] = {
        "aaa", "aaa", "bbb", "bbb", "bbb", "bbb", "aaa"
    };
    assert(strcmp(mode(arr_str1, sizeof(arr_str1) / sizeof(arr_str1[0])), "bbb") == 0);
    char *arr_str2[] = {
        "aaa", "aaa", "bbb", "bbb", "bbb", "bbb", "aaa", "cc", "cc", "cc", "cc", "cc", "cc",
    };
    assert(strcmp(mode(arr_str2, sizeof(arr_str2) / sizeof(arr_str2[0])), "cc") == 0);

    printf("Every test in C for StatFuncs library was successful\n");

    return 0;
}
