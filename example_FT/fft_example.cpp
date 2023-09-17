#include <Eigen/Dense>
#include <unsupported/Eigen/FFT>
#include <vector>

extern "C" {
    void fft_2d_eigen(double* in, std::complex<double>* out, int rows, int cols) {
        Eigen::MatrixXd in_matrix(rows, cols);
        Eigen::MatrixXcd out_matrix(rows, cols);
        Eigen::FFT<double> fft;

        // Fill the input matrix
        int k = 0;
        for(int i = 0; i < rows; ++i) {
            for(int j = 0; j < cols; ++j) {
                in_matrix(i, j) = in[k++];
            }
        }

        // Perform 2D FFT
        for(int i = 0; i < rows; ++i) {
            Eigen::VectorXd in_row = in_matrix.row(i);
            Eigen::VectorXcd out_row(cols);
            fft.fwd(out_row, in_row);
            out_matrix.row(i) = out_row;
        }

        for(int i = 0; i < cols; ++i) {
            Eigen::VectorXcd in_col = out_matrix.col(i);
            Eigen::VectorXcd out_col(rows);
            fft.fwd(out_col, in_col);
            out_matrix.col(i) = out_col;
        }

        // Fill the output array
        k = 0;
        for(int i = 0; i < rows; ++i) {
            for(int j = 0; j < cols; ++j) {
                out[k++] = out_matrix(i, j);
            }
        }
    }
}
