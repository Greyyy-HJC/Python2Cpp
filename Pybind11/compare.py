import numpy as np
import time
import sys
sys.path.append('/Users/greyyy/git/Python2Cpp/Pybind11/build')
import fast_loop_module


def slow_loop(arr):
    result = []
    for matrix in arr:
        result.append(np.fft.fft2(matrix))
    return np.array(result)

# Generating a batch of 10 random 1024x1024 matrices
data = np.random.rand(100, 1024, 1024)

# Timing the slow loop (Python/NumPy)
start_time = time.time()
res_slow = slow_loop(data)
print("Slow loop time: ", time.time() - start_time, " seconds")

# Timing the fast loop (C++/FFTW)
start_time = time.time()
res_fast = fast_loop_module.fast_loop(data)
print("Fast loop time: ", time.time() - start_time, " seconds")
