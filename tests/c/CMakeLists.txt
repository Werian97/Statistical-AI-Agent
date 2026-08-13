add_executable(test_c_library)

target_sources(test_c_library
    PRIVATE
        test_c_library.c
)

target_link_libraries(test_c_library
    PRIVATE
        StatFuncs
)