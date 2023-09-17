#include <Eigen/Dense>
#include <complex>

extern "C" {
void fourier(double* lam, double* fz_real, double* fz_imag, int len_fz, double* x, int len_x, double* output_real, double* output_imag) {
  Eigen::Map<Eigen::VectorXd> lam_map(lam, len_fz);
  Eigen::Map<Eigen::VectorXd> fz_real_map(fz_real, len_fz);
  Eigen::Map<Eigen::VectorXd> fz_imag_map(fz_imag, len_fz);
  Eigen::VectorXcd            fz_map(len_fz);


  for (int i = 0; i < len_fz; i++) {
    fz_map[i] = std::complex<double>(fz_real_map[i], fz_imag_map[i]);
  }

  double dlam = lam_map[1] - lam_map[0];


  for (int i = 0; i < len_x; i++) {
    double               xx         = x[i];
    Eigen::VectorXcd     exp_values = (-std::complex<double>(0, 1) * (xx - 0.5) * lam_map).array().exp();
    std::complex<double> result     = dlam / (2 * M_PI) * (fz_map.array() * exp_values.array()).sum();
    output_real[i]                  = result.real();
    output_imag[i]                  = result.imag();
  }
}
}
