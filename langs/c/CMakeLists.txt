cmake_minimum_required(VERSION 3.10)
project(${project_name} C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "-Wall -Wextra")

# Source files
file(GLOB_RECURSE SRC_FILES src/*.c libs/*.c)
file(GLOB_RECURSE HEADER_FILES src/*.h libs/*.h)

# Include directories
include_directories(${PROJECT_SOURCE_DIR}/src ${PROJECT_SOURCE_DIR}/libs)

# Library files
file(GLOB LIB_FILES libs/*/lib/*.a)

# Output executable
add_executable(main ${SRC_FILES})
target_link_libraries(main ${LIB_FILES})

# Set output directory
set_target_properties(main PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)
