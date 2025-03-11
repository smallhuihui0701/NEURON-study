from neuron import h
from neuron.units import µm, ms, mV, cm
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc")

#
# model organism
#

# topology
soma = h.Section("soma")

# morphology
soma.L = 10 * µm
soma.diam = 10 * µm

# biophysics
soma.insert(h.hh)

#
# first experiment: clamp to 0 mV
#
vc = h.SEClamp(soma(0.5))
vc.dur1 = 5 * ms
vc.amp1 = -65 * mV
vc.dur2 = 20 * ms
vc.amp2 = 0 * mV
vc.dur3 = 5 * ms
vc.amp3 = -65 * mV

# recording
t = h.Vector().record(h._ref_t)
v = h.Vector().record(soma(0.5)._ref_v)
ina = h.Vector().record(soma(0.5)._ref_ina)
ik = h.Vector().record(soma(0.5)._ref_ik)

# run
h.finitialize(-65 * mV)
h.continuerun(30 * ms)

#
# plot
#
plt.figure()
plt.plot(t, ina, label="ina")
plt.plot(t, ik, label="ik")
plt.xlabel("time (ms)")
plt.ylabel("current (mA/cm²)")
plt.legend()

#
# second experiment: vary clamping voltage
#
plt.figure()
for vc.amp2 in [-80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40]:
    h.finitialize(-65 * mV)
    h.continuerun(30 * ms)

    plt.plot(t, ik, label=f"v = {vc.amp2} mV")
    plt.xlabel("time (ms)")
    plt.ylabel("ik (mA/cm²)")
    plt.legend()

plt.show()

# Note: to see something interesting, change the continuerun
# duration in line 57 to 50 ms. What happens? Why?