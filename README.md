# NeuroSpike

An interactive implementation of the Leaky Integrate-and-Fire (LIF) neuron built from scratch in Python.

This project demonstrates the fundamental computational unit used in Spiking Neural Networks (SNNs). Unlike traditional Artificial Neural Networks, neurons communicate using discrete spikes over time, making SNNs more biologically realistic and energy efficient.

## Features

- LIF neuron implemented from scratch
- Interactive parameter tuning with Streamlit sliders
- Membrane potential visualization
- Red spike markers on threshold crossings
- Spike train visualization
- Firing rate analysis
- Frequency-Current (F-I) curve
- Time to first spike statistic
- Dark educational interface
- Animation mode that shows voltage evolving step by step
- No SNN frameworks used

## Technologies

- Python
- NumPy
- Matplotlib
- Streamlit

## Project Structure

```text
NeuroSpike/
|-- app.py              # Streamlit application
|-- neuron.py           # LIF neuron implementation
|-- simulation.py       # Simulation engine
|-- simulator.py        # Compatibility exports
|-- plots.py            # Plotting functions
|-- utils.py            # Statistics exports
|-- experiment.py       # Firing-rate experiment helper
|-- network.py          # Simple chained neuron network experiment
|-- main.py             # Command-line demo
|-- requirements.txt
|-- README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

## Run the Command-Line Demo

```bash
python main.py
```

## What I Learned

During this project I learned:

- Leaky Integrate-and-Fire dynamics
- Event-driven computation
- Spike trains
- Numerical simulation
- Membrane potential modelling
- Firing rate analysis
- Computational neuroscience fundamentals

## Screenshots

<img width="1861" height="895" alt="image" src="https://github.com/user-attachments/assets/686ee224-99f2-4cd1-b109-86d3930f0b26" />


```text
assets/screenshot.png
assets/banner.png
```
