import numpy as np

# 1. THE DATA: Define our clean "Qubit" target state (e.g., State |0>)
clean_state = np.array([1.0, 0.0])

# 2. THE NOISE: Maximally Mixed State (The output of the forward diffusion process)
# This represents a system where all quantum information has been destroyed by entropy.
noisy_state = np.array([0.7071, 0.7071])

# 3. THE AI (PQC): Parameterized Quantum Circuit
# This function applies a Unitary Rotation Matrix (Ry) based on a trainable angle (theta).
def apply_recoherence_gate(state, theta):
    rotation_matrix = np.array([
        [np.cos(theta/2), -np.sin(theta/2)],
        [np.sin(theta/2),  np.cos(theta/2)]
    ])
    return np.dot(rotation_matrix, state)

# 4. THE LOSS FUNCTION: Quantum Fidelity
# Measures how perfectly the AI reconstructed the original state (1.0 = perfect).
def calculate_fidelity(state_a, state_b):
    return np.abs(np.dot(state_a, state_b))**2

# ==========================================
# THE TRAINING LOOP (Gradient Descent)
# ==========================================
theta_guess = 3.14  # Start with a terrible, randomized initial guess
learning_rate = 0.1

print("--- Starting QuDDPM Recoherence Training ---")
print(f"Initial Noisy State: {noisy_state}\n")

for epoch in range(50):
    # Forward Pass: AI guesses the clean state by rotating the noisy state
    predicted_state = apply_recoherence_gate(noisy_state, theta_guess)
    
    # Calculate Loss: Check how good the guess was
    fidelity = calculate_fidelity(predicted_state, clean_state)
    
    # Backward Pass: Calculate error and update theta (Gradient Descent)
    error = 1.0 - fidelity
    theta_guess -= learning_rate * error 
    
    # Print progress every 10 epochs
    if epoch % 10 == 0:
        print(f"Epoch {epoch:02d} | Fidelity: {fidelity:.4f} | Angle: {theta_guess:.4f}")

print("\n--- Training Complete. Entropy Reversed. ---")
print(f"Final Reconstructed State: [{predicted_state[0]:.4f}, {predicted_state[1]:.4f}]")
