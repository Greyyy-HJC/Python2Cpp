#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <fftw3.h>
#include <complex>

namespace py = pybind11;

py::array_t<std::complex<double>> fast_loop(py::array_t<double, py::array::c_style | py::array::forcecast> array) {
    py::buffer_info buf_info = array.request();

    if (buf_info.ndim != 3)
        throw std::runtime_error("Number of dimensions must be 3");

    int num_matrices = buf_info.shape[0];
    int rows = buf_info.shape[1];
    int cols = buf_info.shape[2];

    auto result = py::array_t<std::complex<double>>({num_matrices, rows, cols});
    auto res_buf_info = result.request();
    std::complex<double>* res_ptr = static_cast<std::complex<double>*>(res_buf_info.ptr);
    
    fftw_complex* in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * rows * cols);
    fftw_complex* out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * rows * cols);
    fftw_plan p = fftw_plan_dft_2d(rows, cols, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    double* in_ptr = static_cast<double*>(buf_info.ptr);

    for (int i = 0; i < num_matrices; ++i) {
        for (int j = 0; j < rows; ++j) {
            for (int k = 0; k < cols; ++k) {
                int index = i * rows * cols + j * cols + k;
                in[j*cols + k][0] = in_ptr[index];
                in[j*cols + k][1] = 0.0;
            }
        }

        fftw_execute(p);

        for (int j = 0; j < rows; ++j) {
            for (int k = 0; k < cols; ++k) {
                int index = i * rows * cols + j * cols + k;
                res_ptr[index] = std::complex<double>(out[j*cols + k][0], out[j*cols + k][1]);
            }
        }
    }

    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return result;
}

PYBIND11_MODULE(fast_loop_module, m) {
    m.def("fast_loop", &fast_loop, "A function which performs FFT on a batch of matrices");
}
