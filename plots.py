import matplotlib.pyplot as plt
import numpy as np


PLOT_STYLE = {
    "figure.facecolor": "#0e1117",
    "axes.facecolor": "#111827",
    "axes.edgecolor": "#334155",
    "axes.labelcolor": "#e5e7eb",
    "xtick.color": "#cbd5e1",
    "ytick.color": "#cbd5e1",
    "grid.color": "#334155",
    "text.color": "#f8fafc",
}


def _apply_dark_style(ax):
    ax.grid(True, alpha=0.35)
    for spine in ax.spines.values():
        spine.set_color("#334155")


def plot_voltage(simulation, limit=None):
    time = simulation["time"][:limit]
    voltage = simulation["display_voltage"][:limit]
    spikes = simulation["spikes"][:limit]
    threshold = simulation["threshold"]
    spike_times = time[spikes == 1]
    spike_voltages = voltage[spikes == 1]

    with plt.rc_context(PLOT_STYLE):
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(time, voltage, color="#38bdf8", linewidth=2.3, label="Membrane potential")
        ax.axhline(threshold, color="#f97316", linestyle="--", linewidth=1.5, label="Threshold")
        if len(spike_times):
            ax.scatter(spike_times, spike_voltages, color="#ef4444", s=46, zorder=4, label="Spike")
        ax.set_title("Membrane Potential")
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Voltage")
        ax.legend(loc="upper right")
        _apply_dark_style(ax)
        fig.tight_layout()
        return fig


def plot_spikes(simulation, limit=None):
    time = simulation["time"][:limit]
    spikes = simulation["spikes"][:limit]
    spike_times = time[spikes == 1]

    with plt.rc_context(PLOT_STYLE):
        fig, ax = plt.subplots(figsize=(10, 2.6))
        if len(spike_times):
            ax.eventplot(spike_times, colors="#f43f5e", lineoffsets=1, linelengths=0.75, linewidths=2.2)
        ax.set_title("Spike Train")
        ax.set_xlabel("Time (ms)")
        ax.set_yticks([])
        ax.set_ylim(0.4, 1.6)
        _apply_dark_style(ax)
        fig.tight_layout()
        return fig


def plot_fi_curve(currents, rates):
    with plt.rc_context(PLOT_STYLE):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(currents, rates, marker="o", color="#22c55e", linewidth=2.2)
        ax.set_title("Frequency-Current Curve")
        ax.set_xlabel("Input current")
        ax.set_ylabel("Firing rate (Hz)")
        _apply_dark_style(ax)
        fig.tight_layout()
        return fig


def plot_multiple_voltages(v_a, v_b, v_c):
    with plt.rc_context(PLOT_STYLE):
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(np.asarray(v_a), label="Neuron A", color="#38bdf8")
        ax.plot(np.asarray(v_b), label="Neuron B", color="#a78bfa")
        ax.plot(np.asarray(v_c), label="Neuron C", color="#22c55e")
        ax.set_title("Network Membrane Potentials")
        ax.set_xlabel("Time step")
        ax.set_ylabel("Voltage")
        ax.legend()
        _apply_dark_style(ax)
        fig.tight_layout()
        return fig
