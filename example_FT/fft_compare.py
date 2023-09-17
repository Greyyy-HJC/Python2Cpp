# %%
import numpy as np
from ctypes import cdll, c_int, c_double, POINTER
from numpy.ctypeslib import ndpointer

class FourierLib_cpp:
    def __init__(self):
        # Load the shared library
        self.lib = cdll.LoadLibrary('./fft_example.so')

        # Define the function prototype
        self.lib.fft_2d_eigen.argtypes = [
            ndpointer(c_double, flags="C_CONTIGUOUS"), 
            ndpointer(np.complex128, flags="C_CONTIGUOUS"), 
            c_int, 
            c_int
        ]

    def cpp_fft_2d(self, matrix):
        rows, cols = matrix.shape
        in_array = matrix.flatten()
        out_array = np.zeros(rows * cols, dtype=np.complex128)
        
        self.lib.fft_2d_eigen(
            in_array, 
            out_array, 
            c_int(rows), 
            c_int(cols)
        )
        
        return out_array.reshape(rows, cols)




# Example usage
import time
from py_fft import python_fft_2d

if __name__ == "__main__":
    fourier_cpp = FourierLib_cpp()

    # Create a large random matrix
    matrix_ls = [np.random.rand(1024, 1024) for i in range(100)]
    result_python_ls = []
    result_cpp_ls = []

    # Measure the time taken by the Python FFT function
    start_time = time.time()
    for matrix in matrix_ls:
        result_python_ls.append( python_fft_2d(matrix) )
    end_time = time.time()
    print(f"Python FFT Time: {end_time - start_time} seconds")
    
    # Measure the time taken by the C++ FFT function
    start_time = time.time()
    for matrix in matrix_ls:
        result_cpp_ls.append( fourier_cpp.cpp_fft_2d(matrix) )
    end_time = time.time()
    print(f"C++ FFT Time: {end_time - start_time} seconds")

    # Compare the results
    for i in range(len(matrix_ls[:5])):
        print(f"Matrix {i}: {np.allclose(result_python_ls[i], result_cpp_ls[i])}")

# %%
