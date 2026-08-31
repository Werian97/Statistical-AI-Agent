#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <StatFuncs.h>

int main() {
    assert(5 == mysum(2, 3));
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

    printf("Every test in C was successful\n");

    return 0;
}