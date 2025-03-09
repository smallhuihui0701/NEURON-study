from neuron import h, gui  # Ensure NEURON GUI is enabled
import matplotlib.pyplot as plt  # For alternative Matplotlib plotting

# Define simulation parameters
h.tstop = 150  # Simulation duration in ms
h.v_init = -65  # Initial membrane voltage

# Create an axon section
axon = h.Section(name="axon")
axon.L = 1000  # Length of the axon in microns
axon.diam = 10  # Diameter in microns
axon.insert("hh")  # Insert Hodgkin-Huxley ion channels

# Create recording vectors
t_vec = h.Vector()  # Time vector
v_vec = h.Vector()  # Membrane potential vector

# Record time and voltage at the center of the axon
t_vec.record(h._ref_t)
v_vec.record(axon(0.5)._ref_v)

# Initialize and run the simulation
h.finitialize(h.v_init)
h.run()

# **Approach 1: NEURON Graph Window (Manually Updated)**
graph = h.Graph()
graph.size(0, h.tstop, -80, 50)  # Set axis ranges
graph.addvar("v(0.5)")  # Correct way to reference voltage at the middle
graph.exec_menu("View = plot")  # Refresh the plot

# **Approach 2: Matplotlib for Custom Plot**
plt.figure(figsize=(8, 5))
plt.plot(t_vec, v_vec, label="Membrane Potential (mV)")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Membrane Potential Over Time")
plt.legend()
plt.grid()
plt.show()
