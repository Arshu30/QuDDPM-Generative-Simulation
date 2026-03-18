# ⚛️ Quantum Generative AI: Reversing Entropy with QuDDPM

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![C++](https://img.shields.io/badge/C++-Benchmark-orange.svg)
![Status](https://img.shields.io/badge/Status-Simulation_Active-success.svg)

## 📌 Abstract
This repository contains the simulation code for our **Quantum Denoising Diffusion Probabilistic Model (QuDDPM)** project. We demonstrate how the thermodynamic reversal of entropy used in classical Generative AI (like Stable Diffusion) can be mathematically mapped to Unitary transformations in Hilbert Space.

By replacing classical Gaussian noise with a Quantum Depolarizing Channel, we train a Parameterized Quantum Circuit (PQC) to learn the inverse Unitary operations required to recohere a maximally mixed state back into a pure target state.

## 📂 Repository Structure
* `/src/quantum_sim.py`: The core Python implementation of the quantum state vectors, depolarizing noise channels, and the gradient descent optimizer.
* `/src/classical_benchmark.cpp`: A C++ benchmark demonstrating the $O(2^n)$ exponential memory and processing bottlenecks of classical matrix multiplication.
* `/notebooks/QuDDPM_Walkthrough.ipynb`: A step-by-step Jupyter Notebook detailing the mathematical proofs and visualizations.
* `/assets/`: High-resolution graphics from our exhibition poster, including the Fidelity training curves and complexity scaling graphs.

## 🧮 The Mathematics (Quantum Fidelity)
To train the recoherence circuit, we optimize the network by maximizing the Quantum Fidelity between the predicted state $\rho$ and the target state $\sigma$. We use this metric to track the AI's learning progress over time:

$$F(\rho, \sigma) = \left( \text{Tr} \sqrt{\sqrt{\rho}\sigma\sqrt{\rho}} \right)^2$$

## 🚀 How to Run the Python Simulation
Clone the repository and run the main training script to watch the model iteratively reverse the simulated quantum noise via gradient descent:

```bash
git clone [https://github.com/YourUsername/QuDDPM-Generative-Simulation.git](https://github.com/YourUsername/QuDDPM-Generative-Simulation.git)
cd QuDDPM-Generative-Simulation
pip install -r requirements.txt
python src/quantum_sim.py
