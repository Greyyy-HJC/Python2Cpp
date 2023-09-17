# %%
import numpy as np
from py_fourier import fourier


nconf = 1500
zmax = 23
lam = 0.12 / 0.197 * 2.15 * np.arange(zmax)
fz_r = np.random.rand(nconf, zmax)
fz_i = np.random.rand(nconf, zmax)
x = -0.5 + 0.01 * np.arange(201)

fp_r, fp_i = fourier(lam, fz_r, fz_i, x)


import ctypes


# Load the shared library and set the function signature
class FourierLib:
    def __init__(self, path="./matrix_fourier.so"):
        self.lib = ctypes.CDLL(path)
        self._set_argtypes()

    def _set_argtypes(self):
        argtype = np.ctypeslib.ndpointer(dtype=np.double, flags="C_CONTIGUOUS")
        self.lib.fourier.argtypes = [
            argtype,
            argtype,
            argtype,
            ctypes.c_int,
            argtype,
            ctypes.c_int,
            argtype,
            argtype,
        ]

    def fourier(self, lam, fz_r, fz_i, x):
        len_fz = len(fz_r)
        len_x = len(x)

        # Create empty arrays for output
        output_real = np.empty(len_x, dtype=np.double)
        output_imag = np.empty(len_x, dtype=np.double)

        # Call the C++ function
        self.lib.fourier(lam, fz_r, fz_i, len_fz, x, len_x, output_real, output_imag)

        return output_real, output_imag


import timeit


start = timeit.default_timer()
fourier_lib = FourierLib()
for i in range(nconf):
    fp_r_c, fp_i_c = fourier_lib.fourier(lam, fz_r[i, :], fz_i[i, :], x)
end = timeit.default_timer()
print("cpp time:" + str(end - start) + "s")


start = timeit.default_timer()
for i in range(nconf):
    fp_r_py, fp_i_py = fourier(lam, fz_r[i, :], fz_i[i, :], x)
end = timeit.default_timer()
print("python time:" + str(end - start) + "s")


print("max error:" + str(np.max(np.abs(fp_r_c - fp_r_py))))


# %%
