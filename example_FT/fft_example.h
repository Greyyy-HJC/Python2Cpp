#ifndef FFT_EXAMPLE_H
#define FFT_EXAMPLE_H

extern "C" {
    void fourier_transform_2d(double* in, double* out, int rows, int cols);
}

#endif // FFT_EXAMPLE_H
