target_sources(StatFuncs
    PRIVATE
        StatFuncs.c
        utility_functions.c
)

add_library(utility_functions)

target_sources(utility_functions
    PRIVATE
        utility_functions.c
    PUBLIC
        FILE_SET HEADERS
        FILES
            utility_functions.h
)