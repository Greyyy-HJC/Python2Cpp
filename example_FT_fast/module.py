import ctypes
import numpy as np

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