import ctypes
import python_API.C_lib_API as clib

def mysum(a: int, b: int) :
    return clib.c_mysum(a,b)

def mean(l: list[float]):
    size: int = len(l)
    arr = ctypes.c_double * size
    c_list = arr(*l)
    return clib.c_mean(c_list, size)