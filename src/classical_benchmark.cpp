#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

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
    cout << "=== Classical Matrix Multiplication Benchmark ===" << endl;

    int N = 1024; // Simulating a 10-qubit Hilbert space dimension (2^10)
    
    vector<vector<double>> matrixA(N, vector<double>(N, 0.5));
    vector<vector<double>> matrixB(N, vector<double>(N, 0.5));
    vector<vector<double>> resultMatrix(N, vector<double>(N, 0.0));

    cout << "Matrix dimension: " << N << "x" << N << endl;
    cout << "Executing O(N^3) classical multiplication pass..." << endl;

    auto start = high_resolution_clock::now();
    multiplyMatrices(matrixA, matrixB, resultMatrix, N);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);

    cout << "Execution completed successfully." << endl;
    cout << "Time elapsed: " << duration.count() << " ms" << endl;

    return 0;
}
