cmake_minimum_required(VERSION 3.14)
project(cpptests)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

# Fetch and download Google Test
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/b796f7d44681514f58a683a3a71ff17c94edb0c1.zip
)
# Windows: Prevent overriding the parent project's compiler/linker settings
# Currently no parent CMake project, but good to keep for the future
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Download MurTree if necessary
set (MURTREE_SOURCE_DIR "${CMAKE_SOURCE_DIR}/../../murtree/code/MurTree/")
if (NOT EXISTS ${MURTREE_SOURCE_DIR})
    FetchContent_Declare(
      murtree
      URL https://github.com/MurTree/dcctree/archive/refs/heads/develop.zip
    )
    FetchContent_Populate(murtree)
    set (MURTREE_SOURCE_DIR ${murtree_SOURCE_DIR}/code/MurTree/)
endif()

# Enable testing in CMake
enable_testing()

include_directories(
    ${CMAKE_SOURCE_DIR}/../../src/pymurtree
    ${MURTREE_SOURCE_DIR}Engine
    ${MURTREE_SOURCE_DIR}Utilities
    "${MURTREE_SOURCE_DIR}Data Structures"
)

add_executable(
    testexporttree
    testexporttree.cpp
    ${CMAKE_SOURCE_DIR}/../../src/pymurtree/exporttree.cpp
)

target_link_libraries(
    testexporttree
    GTest::gtest_main
)

# Enable CMake’s test runner to discover the tests included in the binary,
# using the GoogleTest CMake module.
include(GoogleTest)
gtest_discover_tests(testexporttree)
