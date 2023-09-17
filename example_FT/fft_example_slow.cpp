#include "fft_example.h"
#include <fftw3.h>
#include <iostream>
#include <cstring>

extern "C" {
    void fourier_transform_2d(double* in, double* out, int rows, int cols) {
        fftw_complex* in_complex = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * rows * cols);
        fftw_complex* out_complex = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * rows * cols);

        for(int i = 0; i < rows * cols; i++) {
            in_complex[i][0] = in[i];
            in_complex[i][1] = 0.0;
        }

        fftw_plan p = fftw_plan_dft_2d(rows, cols, in_complex, out_complex, FFTW_FORWARD, FFTW_ESTIMATE);

        fftw_execute(p);

        for(int i = 0; i < rows * cols; i++) {
            out[i*2] = out_complex[i][0];
            out[i*2+1] = out_complex[i][1];
        }

        fftw_destroy_plan(p);
        fftw_free(in_complex);
        fftw_free(out_complex);
    }
}
