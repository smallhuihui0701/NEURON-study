from neuron import h, gui  # Import NEURON with GUI support

# Create a single axon section
axon = h.Section(name="axon")
axon.L = 1000  # Axon length (in microns)
axon.diam = 10  # Axon diameter (in microns)
axon.insert("hh")  # Insert Hodgkin-Huxley channels

# Apply a stimulus (current injection) to generate an AP
stim = h.IClamp(axon(0.5))  # Place the stimulus in the middle of the axon
stim.delay = 1  # Stimulus starts at 1 ms
stim.dur = 1  # Duration of stimulus (1 ms)
stim.amp = 2.0  # Amplitude of injected current (nA) - Increased to 2 nA

# Set up vectors for recording time and voltage
t_vec = h.Vector()  # Time vector
v_vec = h.Vector()  # Membrane potential vector

# Record time and voltage at the center of the axon (axon(0.5))
t_vec.record(h._ref_t)
v_vec.record(axon(0.5)._ref_v)

# **Simulation parameters**
h.tstop = 40  # Simulation time (ms)
h.dt = 0.025  # Time step (ms)
h.finitialize(-65)  # Initialize with resting potential (-65 mV)

# Create a NEURON graph window
graph = h.Graph()
graph.size(0, h.tstop, -80, 50)  # Set axis range (time: 0-40 ms, voltage: -80 to 50 mV)
graph.addvar("v(0.5)", axon(0.5)._ref_v)  # Correctly link voltage to the graph
graph.exec_menu("Keep Lines")  # Enable "Keep Lines" mode to overlay traces

# **Run the simulation**
print("Simulation starting...")
h.run()

# Force the graph to update
graph.flush()

# **Plot the recorded data for verification using Matplotlib**
import matplotlib.pyplot as plt
plt.plot(t_vec, v_vec)
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.title('Membrane Potential vs Time (from Python)')
plt.grid()
plt.show()

# **Pause the script to keep the GUI open**
input("Simulation complete. Press Enter to close the NEURON GUI...")