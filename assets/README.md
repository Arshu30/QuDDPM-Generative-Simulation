# ⚛️ Quantum Generative AI: Reversing Entropy with QuDDPM

An optimization and simulation framework for Quantum Denoising Diffusion Probabilistic Models (QuDDPM). This repository demonstrates how the thermodynamic reversal of entropy used in classical Generative AI (like Stable Diffusion) can be mathematically mapped onto unitary transformations in Hilbert space.

By replacing classical Gaussian noise with a Quantum Depolarizing Channel, this implementation models state degradation and trains a Parameterized Quantum Circuit (PQC) optimized via the analytical Parameter-Shift Rule to learn the inverse operations required to recohere a mixed state back into a pure target state vector.

---

## 📚 References & Literature Review

**Research Papers:**
* [1] *Denoising Diffusion Probabilistic Models. Advances in Neural Information Processing Systems (NeurIPS).
* [2] *Diffusion Models Beat GANs on Image Synthesis.
* [3] *High-Resolution Image Synthesis with Latent Diffusion Models. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
* [4] *Quantum Diffusion Models. (arXiv:2308.12013).
* [5] *Enhancing Quantum Diffusion Models for Image Generation.
* [6] *Measurement-Based Quantum Diffusion Models. (arXiv:2508.08799).

**Lectures & Breakdowns:**
* 🎥 [DDPM - Diffusion Models Beat GANs on Image Synthesis](https://youtu.be/W-O7AZNzbzQ) (Yannic Kilcher's breakdown of the classical forward/reverse Markov chains).
* 🎥 [Generative Quantum Machine Learning via Denoising Diffusion Probabilistic Models] (https://youtu.be/zXR9Etnlw-0?si=IGqJEhafO_ziCuHb).

> **Note:** The PDF versions of these research papers are available in the `/references/` directory of this repository for offline review.

## 🚀 Core Architecture

1. **Analytical Gradient Engine (`src/quantum_sim.py`)**: Implements exact quantum gradient tracking via the Parameter-Shift Rule. It evaluates analytical partial derivatives by executing shifted parameter passes ($\theta \pm \frac{\pi}{2}$) to optimize gate rotations via Gradient Ascent without relying on classical backpropagation heuristics.
2. **Interactive Visualizer (`src/ui.py`)**: A reactive Streamlit dashboard utilizing Plotly to render real-time state fidelity convergence curves and gradient magnitudes across optimization epochs.
3. **Complexity Benchmark (`src/classical_benchmark.cpp`)**: A C++ executable demonstrating the exponential $O(2^n)$ memory allocation and $O(N^3)$ computational bottlenecks encountered when simulating high-dimensional Hilbert spaces classically.

---

## 📌 Abstract
This repository contains the simulation code for our **Quantum Denoising Diffusion Probabilistic Model (QuDDPM)** project. We demonstrate how the thermodynamic reversal of entropy used in classical Generative AI (like Stable Diffusion) can be mathematically mapped to Unitary transformations in Hilbert Space.

By replacing classical Gaussian noise with a Quantum Depolarizing Channel, we train a Parameterized Quantum Circuit (PQC) to learn the inverse Unitary operations required to recohere a maximally mixed state back into a pure target state.


# 📂 Repository Structure

```text
QuDDPM-Generative-Simulation/
│
├── src/
│   ├── quantum_sim.py          # Analytical parameter-shift optimization loop
│   ├── ui.py                   # Streamlit reactive dashboard & plotting suite
│   └── classical_benchmark.cpp # C++ O(N^3) matrix multiplication benchmark
│
├── notebooks/
│   └── QuDDPM_Walkthrough.ipynb # Mathematical proofs and step-by-step derivations
│
├── assets/                     # Refrence research papers
└── requirements.txt            # Python dependency manifest
```

🧮 The Mathematics (Quantum Fidelity & Gradients)The optimization landscape maximizes the Quantum Fidelity ($F$) between the time-evolved predicted state vector $|\psi(\theta)\rangle$ and the target pure state $|\phi\rangle$:$$F(\rho, \sigma) = \left( \text{Tr} \sqrt{\sqrt{\rho}\sigma\sqrt{\rho}} \right)^2$$Because classical automatic differentiation cannot be evaluated directly on physical quantum processors, the exact analytical gradient with respect to the gate parameter $\theta$ is computed using the Parameter-Shift Rule:$$\frac{\partial F}{\partial \theta} = \frac{1}{2} \left[ F\left(\theta + \frac{\pi}{2}\right) - F\left(\theta - \frac{\pi}{2}\right) \right]$$The parameter updates are then applied iteratively via gradient ascent:$$\theta \leftarrow \theta + \eta \frac{\partial F}{\partial \theta}$$


💻 Execution Instructions
1. Classical Matrix Complexity Benchmark
To compile and run the native C++ benchmark validating the exponential runtime limits of classical simulation architectures:

Bash
g++ -O3 src/classical_benchmark.cpp -o benchmark
./benchmark
2. Quantum Simulation CLI
To run the core analytical parameter-shift optimization loop directly within the terminal:

Bash
python src/quantum_sim.py
3. Interactive Plotly Dashboard
To launch the responsive graphical interface tracking optimization trajectories and convergence metrics:

Bash
pip install -r requirements.txt
streamlit run src/ui.py

