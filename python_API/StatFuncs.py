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