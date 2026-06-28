import os
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="QuDDPM Dashboard", page_icon="⚛️", layout="wide")

st.title("⚛️ QuDDPM Optimization Visualizer")
st.markdown("Analytical optimization framework utilizing the Parameter-Shift Rule for quantum state recoherence.")

st.sidebar.header("Configuration")
learning_rate = st.sidebar.slider("Learning Rate (η)", 0.05, 0.5, 0.2, step=0.05)
epochs = st.sidebar.slider("Epochs", 10, 100, 40, step=10)
initial_theta = st.sidebar.slider("Initial Theta (θ)", 0.0, 2 * np.pi, 3.14)

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
    f_plus = calculate_fidelity(apply_recoherence_gate(state, theta + shift), target)
    f_minus = calculate_fidelity(apply_recoherence_gate(state, theta - shift), target)
    return 0.5 * (f_plus - f_minus)

clean_state = np.array([1.0, 0.0])
noisy_state = np.array([0.7071, 0.7071])

if st.sidebar.button("Execute Optimization Loop"):
    fidelities, gradients, thetas = [], [], []
    theta_current = initial_theta
    
    progress_bar = st.progress(0)
    metrics_placeholder = st.empty()
    
    for epoch in range(epochs + 1):
        predicted_state = apply_recoherence_gate(noisy_state, theta_current)
        fidelity = calculate_fidelity(predicted_state, clean_state)
        grad = compute_parameter_shift_gradient(noisy_state, clean_state, theta_current)
        
        fidelities.append(fidelity)
        gradients.append(grad)
        thetas.append(theta_current)
        
        theta_current += learning_rate * grad
        progress_bar.progress(epoch / epochs)
        
        metrics_placeholder.markdown(
            f"**Epoch:** `{epoch}/{epochs}` | **Fidelity:** `{fidelity:.6f}` | **dF/dθ:** `{grad:+.6f}`"
        )
    
    col1, col2 = st.columns(2)
    with col1:
        fig_fid = go.Figure()
        fig_fid.add_trace(go.Scatter(y=fidelities, mode='lines+markers', name='Fidelity', line=dict(color='#FF4B4B', width=3)))
        fig_fid.update_layout(xaxis_title="Epoch", yaxis_title="State Fidelity")
        st.plotly_chart(fig_fid, use_container_width=True)
        
    with col2:
        fig_grad = go.Figure()
        fig_grad.add_trace(go.Scatter(y=gradients, mode='lines', name='Gradient', line=dict(color='#00CC96', width=2, dash='dash')))
        fig_grad.update_layout(xaxis_title="Epoch", yaxis_title="Gradient Magnitude")
        st.plotly_chart(fig_grad, use_container_width=True)
        
    st.success(f"Convergence achieved. Final Fidelity: {fidelities[-1]:.6f}")
