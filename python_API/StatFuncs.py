import os
import ctypes

test_file_path: str = os.path.abspath(".")
shared_lib_path: str = os.path.join(test_file_path, "build/libStatFuncs.so")
C_Library = ctypes.CDLL(shared_lib_path)
mysum = C_Library.mysum
mysum.argtypes = [ctypes.c_int, ctypes.c_int]
mysum.restype = ctypes.c_int