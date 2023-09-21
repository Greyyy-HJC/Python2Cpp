# %%
import numpy as np
from py_fourier import fourier


# Set the value of nconf to 1500
nconf = 1500

# Set the value of zmax to 23
zmax = 23

# Calculate the values of lam using the formula 0.12 / 0.197 * 2.15 * np.arange(zmax)
lam = 0.12 / 0.197 * 2.15 * np.arange(zmax)

# Generate a random array fz_r with shape (nconf, zmax)
fz_r = np.random.rand(nconf, zmax)

# Generate a random array fz_i with shape (nconf, zmax)
fz_i = np.random.rand(nconf, zmax)

# Generate an array x with values ranging from -0.5 to 2.0 with a step size of 0.01 and shape (201,)
x = -0.5 + 0.01 * np.arange(201)

# Call the function fourier with the arguments lam, fz_r, fz_i, and x and assign the returned values to fp_r and fp_i
fp_r, fp_i = fourier(lam, fz_r, fz_i, x)


from module import FourierLib
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
