cmake_minimum_required(VERSION 3.12)
project(fast_loop_module)

set(CMAKE_CXX_STANDARD 14)

find_package(pybind11 REQUIRED)

set(FFTW3_INCLUDE_DIRS "/opt/homebrew/opt/fftw/include")
set(FFTW3_LIBRARIES "/opt/homebrew/opt/fftw/lib/libfftw3.a")

include_directories(${FFTW3_INCLUDE_DIRS})

add_library(fast_loop_module MODULE fast_loop.cpp)
target_link_libraries(fast_loop_module PRIVATE pybind11::module ${FFTW3_LIBRARIES})
