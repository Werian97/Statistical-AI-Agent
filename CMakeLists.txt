cmake_minimum_required(VERSION 3.23)

project("Statistical Functions in C")

add_library(StatFuncs SHARED)

add_subdirectory(src)
add_subdirectory(include)
add_subdirectory(tests/c)
