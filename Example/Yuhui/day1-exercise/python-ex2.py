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
axon.L = 0.1 * cm  # shorter than in my python-ex1 
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
t = h.Vector().record(h._ref_t)
v = h.Vector().record(axon(0.5)._ref_v)
ina = h.Vector().record(axon(0.5)._ref_ina)
ik = h.Vector().record(axon(0.5)._ref_ik)

#
# run
#
plt.figure()
h.finitialize(-65 * mV)
h.continuerun(32 * ms)

plt.subplot(211)
plt.plot(t, v, label="v")
plt.ylabel("v (mV)")
plt.subplot(212)
plt.plot(t, ina, label="ina")
plt.plot(t, ik, label="ik")
plt.ylabel("i (mA/cm^2)")
plt.legend()

plt.show()
