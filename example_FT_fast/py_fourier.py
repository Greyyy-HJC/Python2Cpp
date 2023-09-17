import numpy as np

def fourier(lam,fz_r,fz_i,x):
    fourier_len = x.shape[0]
    fp_r = np.zeros((fourier_len)) ; fp_i = np.zeros((fourier_len))
    for i in range(fourier_len):
        xx = x[i] ; dlam = lam[1]-lam[0] ; phase = -(xx-0.5)*lam
        fp_r[i] = dlam/(2*np.pi)*np.sum(fz_r*np.cos(phase)-fz_i*np.sin(phase))
        fp_i[i] = dlam/(2*np.pi)*np.sum(fz_r*np.sin(phase)+fz_i*np.cos(phase))
    return fp_r,fp_i
