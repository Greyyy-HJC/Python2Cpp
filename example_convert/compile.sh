# g++ -I/opt/homebrew/Cellar/eigen/3.4.0_1/include/eigen3 -shared -o invert_matrix.so -fPIC invert_matrix.cpp

g++ -I/opt/homebrew/Cellar/eigen/3.4.0_1/include/eigen3 -O3 -flto -ffast-math -std=c++11 -shared -o invert_matrix.so -fPIC invert_matrix.cpp
