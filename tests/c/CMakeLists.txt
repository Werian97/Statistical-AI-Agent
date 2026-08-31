add_executable(test_c_library)

target_sources(test_c_library
    PRIVATE
        test_c_library.c
)

target_link_libraries(test_c_library
    PRIVATE
        StatFuncs
)

add_executable(test_utility_functions)

target_sources(test_utility_functions
    PRIVATE
        test_utility_functions.c
)

target_link_libraries(test_utility_functions
    PRIVATE
        utility_functions
)