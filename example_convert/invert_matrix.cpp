#include <Eigen/Dense>
#include <iostream>

extern "C" {
    void invert_matrix(double* in, double* out, int rows, int cols) {
        Eigen::MatrixXd mat(rows, cols);
        Eigen::MatrixXd inv(rows, cols);

        int k = 0;
        for(int i = 0; i < rows; ++i) {
            for(int j = 0; j < cols; ++j) {
                mat(i, j) = in[k++];
            }
        }

        inv = mat.inverse();

        k = 0;
        for(int i = 0; i < rows; ++i) {
            for(int j = 0; j < cols; ++j) {
                out[k++] = inv(i, j);
            }
        }
    }
}
