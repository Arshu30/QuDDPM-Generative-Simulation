import numpy as np
clean_state = np.array([1.0, 0.0])
noisy_state = np.array([0.7071, 0.7071])  
def apply_recoherence_gate(state, theta):
    rotation_matrix = np.array([
        [np.cos(theta / 2), -np.sin(theta / 2)],
        [np.sin(theta / 2),  np.cos(theta / 2)]
    ])
    return np.dot(rotation_matrix, state)


def calculate_fidelity(state_a, state_b):
    return np.abs(np.dot(state_a, state_b)) ** 2

def compute_parameter_shift_gradient(state, target, theta):
    shift = np.pi / 2
    
    
    state_plus = apply_recoherence_gate(state, theta + shift)
    f_plus = calculate_fidelity(state_plus, target)
    
   
    state_minus = apply_recoherence_gate(state, theta - shift)
    f_minus = calculate_fidelity(state_minus, target)
    
  
    gradient = 0.5 * (f_plus - f_minus)
    return gradient


theta_guess = 3.14 
learning_rate = 0.2
epochs = 51

print("--- Starting QuDDPM Analytical Parameter-Shift Training ---")
print(f"Initial Noisy State Vector: {noisy_state}")
print(f"Target Pure State Vector:    {clean_state}\n")

for epoch in range(epochs):
    # Forward Pass: Compute current generation trajectory
    predicted_state = apply_recoherence_gate(noisy_state, theta_guess)
    fidelity = calculate_fidelity(predicted_state, clean_state)
    
    # Compute Exact Quantum Gradient (Maximizing Fidelity via Gradient Ascent)
    grad = compute_parameter_shift_gradient(noisy_state, clean_state, theta_guess)
    
    # Update gate parameter using analytical derivative
    theta_guess += learning_rate * grad
    
    # Log optimization trajectory checkpoints
    if epoch % 10 == 0:
        print(f"Epoch {epoch:02d} | Fidelity: {fidelity:.6f} | dF/d_theta: {grad:+.6f} | Theta: {theta_guess:.4f}")

print("\n--- Training Complete. Hilbert Space Vector Restored. ---")
print(f"Final Reconstructed State: [{predicted_state[0]:.4f}, {predicted_state[1]:.4f}]")
print(f"Target Clean State Vector:  [{clean_state[0]:.4f}, {clean_state[1]:.4f}]")
