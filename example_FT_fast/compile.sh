# g++ -I/opt/homebrew/Cellar/eigen/3.4.0_1/include/eigen3 -shared -o matrix_fourier.so -fPIC matrix_fourier.cpp   # slow

g++ -I/opt/homebrew/Cellar/eigen/3.4.0_1/include/eigen3 -O3 -funroll-loops -std=c++11 -shared -o matrix_fourier.so -fPIC matrix_fourier.cpp    # fast
