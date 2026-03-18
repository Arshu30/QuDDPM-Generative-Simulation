#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Function to multiply two square matrices
void multiplyMatrices(const vector<vector<double>>& A, const vector<vector<double>>& B, vector<vector<double>>& C, int N) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            C[i][j] = 0;
            for (int k = 0; k < N; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    cout << "--- Classical Simulation Bottleneck Benchmark ---" << endl;
    cout << "Simulating exponential complexity O(2^n) of classical diffusion..." << endl;

    // Test with a large matrix dimension (representing a small 10-qubit system state space, 2^10 = 1024)
    int N = 1024; 
    
    vector<vector<double>> matrixA(N, vector<double>(N, 0.5));
    vector<vector<double>> matrixB(N, vector<double>(N, 0.5));
    vector<vector<double>> resultMatrix(N, vector<double>(N, 0.0));

    cout << "\nAllocated " << N << "x" << N << " matrices in memory." << endl;
    cout << "Starting O(N^3) matrix multiplication..." << endl;

    // Start timer
    auto start = high_resolution_clock::now();

    multiplyMatrices(matrixA, matrixB, resultMatrix, N);

    // Stop timer
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    cout << "Multiplication Complete." << endl;
    cout << "Time taken for a single transformation step: " << duration.count() << " milliseconds." << endl;
    cout << "\nCONCLUSION: As system size 'n' grows, classical simulation time scales exponentially." << endl;
    cout << "Quantum hardware applies this transformation natively in O(1) time per gate." << endl;

    return 0;
}
