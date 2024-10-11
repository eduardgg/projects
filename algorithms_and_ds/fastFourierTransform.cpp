#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/FFT>
#include <complex>
#include <vector>

using namespace std;

// Funció per a calcular la convolució de dos vectors utilitzant la FFT
vector<complex<float>> convolution(const vector<complex<float>>& x, const vector<complex<float>>& y) {
    int n = x.size() + y.size() - 1;
    int fftSize = 1;
    while (fftSize < n) {
        fftSize *= 2;
    }

    // Extreiem els nombres complexos dels vectors d'entrada i omplim amb zeros si cal
    Eigen::VectorXcf X(fftSize);
    X.head(x.size()) = Eigen::Map<const Eigen::VectorXcf>(x.data(), x.size());
    X.tail(fftSize - x.size()).setZero();

    Eigen::VectorXcf Y(fftSize);
    Y.head(y.size()) = Eigen::Map<const Eigen::VectorXcf>(y.data(), y.size());
    Y.tail(fftSize - y.size()).setZero();

    // Calcul de la FFT
    Eigen::FFT<float> fft;
    Eigen::VectorXcf X_fft, Y_fft;
    fft.fwd(X_fft, X);
    fft.fwd(Y_fft, Y);

    // Producte de la FFTs
    Eigen::VectorXcf result_fft = X_fft.cwiseProduct(Y_fft);

    // Calcul de la inversa de la FFT
    Eigen::VectorXcf result;
    fft.inv(result, result_fft);

    // Convertim el resultat a vector de complex<float>
    vector<complex<float>> convolutionResult;
    for (int i = 0; i < n; ++i) {
        convolutionResult.push_back(result[i]);
    }

    return convolutionResult;
}

int main() {
    // Vectors d'entrada
    vector<complex<float>> x = {1, 2, 3, 4};
    vector<complex<float>> y = {1, 1, 1};

    // Calcul de la convolució
    vector<complex<float>> result = convolution(x, y);

    // Imprimim el resultat
    cout << "Convolució: ";
    for (auto& val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
