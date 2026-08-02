import time

import numpy as np
import streamlit as st

from plots import plot_fi_curve, plot_spikes, plot_voltage
from simulation import compute_statistics, run_fi_curve, run_lif_simulation


st.set_page_config(
    page_title="NeuroSpike",
    page_icon="NeuroSpike",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    .stApp {
        background: #0e1117;
        color: #f8fafc;
    }
    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }
    div[data-testid="stMetric"] {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 8px;
        padding: 0.75rem 0.9rem;
    }
    .hero {
        border-bottom: 1px solid #263244;
        margin-bottom: 1.1rem;
        padding-bottom: 0.8rem;
    }
    .equation-panel {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 0.5rem;
    }
    .theory {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 8px;
        padding: 1rem 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="hero">
        <h1>NeuroSpike</h1>
        <p>Interactive Leaky Integrate-and-Fire neuron simulator</p>
    </div>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.header("Parameters")
    input_current = st.slider("Input current", 0.0, 3.0, 1.2, 0.05)
    threshold = st.slider("Threshold", 0.5, 5.0, 2.0, 0.05)
    tau = st.slider("Membrane time constant tau", 1.0, 60.0, 20.0, 1.0)
    resistance = st.slider("Membrane resistance", 1.0, 25.0, 10.0, 0.5)
    simulation_time = st.slider("Simulation time (ms)", 50, 1000, 300, 25)
    reset_potential = st.slider("Reset potential", -1.0, 1.0, 0.0, 0.05)
    resting_potential = st.slider("Resting potential", -1.0, 1.0, 0.0, 0.05)
    animation_mode = st.toggle("Animation mode", value=False)
    animation_speed = st.slider("Animation speed", 5, 80, 25, 5, disabled=not animation_mode)


simulation = run_lif_simulation(
    input_current=input_current,
    simulation_time=simulation_time,
    threshold=threshold,
    reset_potential=reset_potential,
    resting_potential=resting_potential,
    membrane_resistance=resistance,
    membrane_time_constant=tau,
)
stats = compute_statistics(simulation)


top_left, top_right = st.columns([2.2, 1])

with top_left:
    st.subheader("Voltage Plot")
    if animation_mode:
        placeholder = st.empty()
        step = max(1, len(simulation["time"]) // animation_speed)
        for frame in range(step, len(simulation["time"]) + step, step):
            placeholder.pyplot(plot_voltage(simulation, limit=frame), clear_figure=True)
            time.sleep(0.03)
    else:
        st.pyplot(plot_voltage(simulation), clear_figure=True)

    st.subheader("Spike Train")
    st.pyplot(plot_spikes(simulation), clear_figure=True)

with top_right:
    st.subheader("Statistics")
    st.metric("Total spikes", stats["total_spikes"])
    st.metric("Firing rate", f"{stats['firing_rate']:.1f} Hz")
    st.metric("Peak voltage", f"{stats['peak_voltage']:.2f}")
    st.metric("Average voltage", f"{stats['average_voltage']:.2f}")
    first_spike = stats["time_to_first_spike"]
    st.metric("Time to first spike", "No spike" if first_spike is None else f"{first_spike:.0f} ms")

    st.markdown(
        f"""
        <div class="equation-panel">
            <h4>Equation</h4>
            <p><code>dV/dt = (-(V - Vrest) + RI) / tau</code></p>
            <p><b>Current voltage:</b> {simulation["voltage"][-1]:.2f}</p>
            <p><b>Current:</b> {input_current:.2f}</p>
            <p><b>Tau:</b> {tau:.0f}</p>
            <p><b>Threshold:</b> {threshold:.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.subheader("F-I Curve")
currents = np.linspace(0.0, 3.0, 16)
fi_currents, rates = run_fi_curve(
    currents,
    simulation_time=simulation_time,
    threshold=threshold,
    reset_potential=reset_potential,
    resting_potential=resting_potential,
    membrane_resistance=resistance,
    membrane_time_constant=tau,
)
st.pyplot(plot_fi_curve(fi_currents, rates), clear_figure=True)


st.subheader("How does this work?")
st.markdown(
    """
    <div class="theory">
        The neuron integrates incoming current over time. Leakage pulls the membrane
        potential back toward rest, while input current pushes it upward. When the
        voltage reaches threshold, the neuron emits a spike, resets, and begins
        integrating again. The spike train shows those discrete firing events.
    </div>
    """,
    unsafe_allow_html=True,
)
