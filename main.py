from simulation import compute_statistics, run_lif_simulation


def main():
    simulation = run_lif_simulation(input_current=1.2, simulation_time=300)
    stats = compute_statistics(simulation)

    print("NeuroSpike command-line demo")
    print(f"Total spikes: {stats['total_spikes']}")
    print(f"Firing rate: {stats['firing_rate']:.1f} Hz")
    print(f"Peak voltage: {stats['peak_voltage']:.2f}")
    print(f"Average voltage: {stats['average_voltage']:.2f}")
    if stats["time_to_first_spike"] is None:
        print("Time to first spike: no spike")
    else:
        print(f"Time to first spike: {stats['time_to_first_spike']:.0f} ms")


if __name__ == "__main__":
    main()
