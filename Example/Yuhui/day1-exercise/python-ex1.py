from neuron import h
from neuron.units import µm, ms, mV, cm
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc")

#
# model organism
#

# topology
axon = h.Section("axon")

# geometry
axon.L = 1 * cm
axon.diam = 1 * µm

# discretization
axon.nseg = 1_001

# dynamics/ion channels/biophysics
h.hh.insert(axon)
axon.Ra = 100  # Ohm cm

#
# experiment
#
ic = h.IClamp(axon(0))
ic.amp = 0.3  # nA
ic.delay = 10 * ms
ic.dur = 0.3 * ms

#
# instrumentation/measurements
#
rvp = h.RangeVarPlot("v", axon(0), axon(1))

#
# run with both Ra = 35.4 and Ra = 100
#
for axon.Ra in [35.4, 100]:
    plt.figure()
    h.finitialize(-65 * mV)
    for tstop in range(8, 32, 2):
        h.continuerun(tstop * ms)
        rvp.plot(plt, label=f"t={h.t:g} ms")

    plt.xlabel("x (µm)")
    plt.ylabel("v (mV)")
    plt.legend()
    plt.title(f"axon.Ra = {axon.Ra} Ohm cm")

plt.show()
