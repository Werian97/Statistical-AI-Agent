import ctypes
import python_API.C_lib_API as clib

def mysum(a: int, b: int) :
    return clib.c_mysum(a,b)

def mean(vector: list[float]):
    size: int = len(vector)
    arr = ctypes.c_double * size
    c_list = arr(*vector)
    return clib.c_mean(c_list, size)

def max(vector: list[float]):
    size: int = len(vector)
    arr = ctypes.c_double * size
    c_list = arr(*vector)
    return clib.c_max(c_list, size)

def min(vector: list[float]):
    size: int = len(vector)
    arr = ctypes.c_double * size
    c_list = arr(*vector)
    return clib.c_min(c_list, size)

def variance(vector: list[float]):
    size: int = len(vector)
    arr = ctypes.c_double * size
    c_list = arr(*vector)
    return clib.c_variance(c_list, size)

def covariance(vector1: list[float], vector2: list[float]):
    size: int = len(vector1)
    if size != len(vector2):
        raise ValueError("Two vectors must ha same size")
    
    arr = ctypes.c_double * size
    c_list1 = arr(*vector1)
    c_list2 = arr(*vector2)
    return clib.c_covariance(c_list1, c_list2, size)