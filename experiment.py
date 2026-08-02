from simulation import compute_statistics, run_lif_simulation


def run_experiment(input_current, simulation_time=1000):
    simulation = run_lif_simulation(input_current=input_current, simulation_time=simulation_time)
    return compute_statistics(simulation)["firing_rate"]
