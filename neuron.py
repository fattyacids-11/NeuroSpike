class LIFNeuron:
    """Leaky Integrate-and-Fire neuron implemented with Euler updates."""

    def __init__(
        self,
        resting_potential=0.0,
        threshold=2.0,
        reset_potential=0.0,
        membrane_resistance=10.0,
        membrane_time_constant=20.0,
        dt=1.0,
    ):
        self.rest = float(resting_potential)
        self.threshold = float(threshold)
        self.reset = float(reset_potential)
        self.R = float(membrane_resistance)
        self.tau = float(membrane_time_constant)
        self.dt = float(dt)
        self.voltage = self.rest

    def reset_state(self):
        self.voltage = self.rest

    def step(self, input_current):
        input_current = float(input_current)
        previous_voltage = self.voltage
        dv = ((-(self.voltage - self.rest) + self.R * input_current) / self.tau) * self.dt
        self.voltage += dv

        spike = 0
        spike_voltage = self.voltage
        if self.voltage >= self.threshold:
            spike = 1
            spike_voltage = self.threshold
            self.voltage = self.reset

        return {
            "voltage": self.voltage,
            "display_voltage": spike_voltage,
            "previous_voltage": previous_voltage,
            "spike": spike,
            "dv": dv,
            "input_current": input_current,
        }
