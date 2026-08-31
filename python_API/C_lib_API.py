import os
import ctypes

test_file_path: str = os.path.abspath(".")
shared_lib_path: str = os.path.join(test_file_path, "build/libStatFuncs.so")
C_Library = ctypes.CDLL(shared_lib_path)

#MYSUM
c_mysum = C_Library.mysum
c_mysum.argtypes = [ctypes.c_int, ctypes.c_int]
c_mysum.restype = ctypes.c_int

#MEAN
c_mean = C_Library.mean
c_mean.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
c_mean.restype = ctypes.c_double

#MAX
c_max = C_Library.max
c_max.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
c_max.restype = ctypes.c_double

#MIN
c_min = C_Library.min
c_min.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
c_min.restype = ctypes.c_double