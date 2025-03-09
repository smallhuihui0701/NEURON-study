from neuron import h, gui
import numpy as np
import matplotlib.pyplot as plt

# Load NEURON standard run library
h.load_file("stdrun.hoc")

# Create the axon
axon = h.Section(name="axon")
axon.L = 20000  # Length in microns (20 mm)
axon.diam = 10  # Diameter in microns
axon.nseg = 100  # Number of segments
axon.Ra = 100  # Axial resistance in Ohm-cm
axon.cm = 1  # Membrane capacitance in uF/cm^2

# Insert Hodgkin-Huxley mechanism
axon.insert("hh")

# Insert extracellular mechanism
axon.insert("extracellular")

# Set extracellular properties for all segments
for seg in axon:
    seg.xraxial[0] = 1e9  # High resistance in axial extracellular space
    seg.xg[0] = 0.0001  # Small conductance to simulate realistic extracellular space
    seg.xc[0] = 0.1  # Small capacitance to simulate realistic extracellular space

# Stimulation (current injection)
stim = h.IClamp(axon(0.1))  # Stimulate at 30% of the axon length
stim.delay = 0.1  # Start stimulation at 0.1 ms
stim.dur = 1  # Duration of stimulation (1 ms)
stim.amp = 1000  # Amplitude of stimulation (800 nA)

# Recording variables
v_vec = h.Vector()  # Membrane potential
t_vec = h.Vector()  # Time vector
ep_vec1 = h.Vector()  # Extracellular potential at location 1
ep_vec2 = h.Vector()  # Extracellular potential at location 2

# Record membrane potential at the middle
v_vec.record(axon(0.75)._ref_v)

# Record time
t_vec.record(h._ref_t)

# Ensure extracellular mechanism is correctly set before recording
ep_vec1.record(axon(0.55)._ref_vext[0])  # Extracellular potential at location 1
ep_vec2.record(axon(0.65)._ref_vext[0])  # Extracellular potential at location 2

# Simulation parameters
h.tstop = 20  # Simulation duration (150 ms)
h.dt = 0.025  # Time step (0.025 ms)
h.v_init = -65  # Initial membrane potential (-65 mV)

# Run simulation
h.run()

# Compute bipolar extracellular potential (difference between the two locations)
bipolar_ep = np.array(ep_vec2) - np.array(ep_vec1)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t_vec, v_vec, label="Membrane Potential (mV)")
plt.plot(t_vec, ep_vec1, label="Extracellular Potential (Location 1)", linestyle="--")
plt.plot(t_vec, ep_vec2, label="Extracellular Potential (Location 2)", linestyle="--")
plt.plot(t_vec, bipolar_ep, label="Bipolar Extracellular Potential (mV)", linewidth=2)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (mV)")
plt.title("Axon Membrane and Extracellular Potentials")
plt.legend()
plt.grid()
plt.show()
