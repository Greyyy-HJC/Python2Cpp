import numpy as np
from ctypes import cdll, c_int, c_double, POINTER

# Load the shared library
lib = cdll.LoadLibrary('./invert_matrix.so')

# Define the function prototype
lib.invert_matrix.argtypes = [
    POINTER(c_double), 
    POINTER(c_double), 
    c_int, 
    c_int
]

def cpp_invert_matrix(matrix):
    rows, cols = matrix.shape
    in_array = matrix.flatten()
    out_array = np.zeros(rows * cols, dtype=np.double)
    
    lib.invert_matrix(
        in_array.ctypes.data_as(POINTER(c_double)), 
        out_array.ctypes.data_as(POINTER(c_double)), 
        c_int(rows), 
        c_int(cols)
    )
    
    return out_array.reshape(rows, cols)

def py_invert_matrix(matrix):
    return np.linalg.inv(matrix)


# Example usage
import time

if __name__ == "__main__":
    # Create a large random matrix
    matrix = np.random.rand(1024, 1024)

    # Measure the time taken by the Python FFT function
    start_time = time.time()
    result_python = py_invert_matrix(matrix)
    end_time = time.time()
    print(f"Python FFT Time: {end_time - start_time} seconds")
    
    # Measure the time taken by the C++ FFT function
    start_time = time.time()
    result_cpp = cpp_invert_matrix(matrix)
    end_time = time.time()
    print(f"C++ FFT Time: {end_time - start_time} seconds")
