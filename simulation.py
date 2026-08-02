import numpy as np

from neuron import LIFNeuron


def run_lif_simulation(
    input_current=1.2,
    simulation_time=300,
    dt=1.0,
    threshold=2.0,
    reset_potential=0.0,
    resting_potential=0.0,
    membrane_resistance=10.0,
    membrane_time_constant=20.0,
):
    """Run a single LIF neuron and return time, voltage, spikes, and metadata."""
    neuron = LIFNeuron(
        resting_potential=resting_potential,
        threshold=threshold,
        reset_potential=reset_potential,
        membrane_resistance=membrane_resistance,
        membrane_time_constant=membrane_time_constant,
        dt=dt,
    )

    steps = int(simulation_time / dt)
    times = np.arange(steps) * dt
    voltages = []
    display_voltages = []
    spikes = []
    dv_values = []

    for _ in range(steps):
        result = neuron.step(input_current)
        voltages.append(result["voltage"])
        display_voltages.append(result["display_voltage"])
        spikes.append(result["spike"])
        dv_values.append(result["dv"])

    return {
        "time": np.array(times),
        "voltage": np.array(voltages),
        "display_voltage": np.array(display_voltages),
        "spikes": np.array(spikes),
        "dv": np.array(dv_values),
        "input_current": input_current,
        "threshold": threshold,
        "reset_potential": reset_potential,
        "resting_potential": resting_potential,
        "membrane_resistance": membrane_resistance,
        "membrane_time_constant": membrane_time_constant,
        "dt": dt,
        "simulation_time": simulation_time,
    }


def compute_statistics(simulation):
    spikes = simulation["spikes"]
    time = simulation["time"]
    voltage = simulation["display_voltage"]
    total_spikes = int(spikes.sum())
    duration_seconds = simulation["simulation_time"] / 1000
    spike_times = time[spikes == 1]

    return {
        "total_spikes": total_spikes,
        "firing_rate": total_spikes / duration_seconds if duration_seconds else 0.0,
        "average_voltage": float(np.mean(voltage)) if len(voltage) else 0.0,
        "peak_voltage": float(np.max(voltage)) if len(voltage) else 0.0,
        "time_to_first_spike": float(spike_times[0]) if len(spike_times) else None,
    }


def run_fi_curve(currents, **simulation_kwargs):
    rates = []
    for current in currents:
        simulation = run_lif_simulation(input_current=current, **simulation_kwargs)
        rates.append(compute_statistics(simulation)["firing_rate"])
    return np.array(currents), np.array(rates)
