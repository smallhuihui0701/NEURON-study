from neuron import h
from neuron.units import ms, mV, µm
h.load_file('stdrun.hoc')

# define a simple model with a soma and a dendrite
class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        soma = h.Section('soma', self)
        soma.L = soma.diam = 10 * µm
        soma.insert(h.hh)
        dend = h.Section('dend', self)
        dend.L = 100 * µm
        dend.diam = 1 * µm
        dend.insert(h.pas)
        dend.connect(soma)
        dend.nseg = 5
        self.soma = soma
        self.dend = dend
        self.soma = soma
        self.dend = dend
        self.syn = h.ExpSyn(dend(0.5))
        self.syn.tau = 2 * ms
        self.syn.e = 0* mV

        for seg in dend:
            seg.pas.e = -65 * mV
        
        # setup recording
        self.v_soma = h.Vector().record(soma(0.5)._ref_v)

    def __repr__(self):
        return f'BallAndStick[{self._gid}]'

cell0 = BallAndStick(0)

#setup stimulation
stim = h.NetStim()
stim.number = 1_000
stim.interval = 50
stim.start = 5 * ms
stim.noise = True

nc = h.NetCon(stim, cell0.syn)
nc.weight[0] = 0.0002 

# control experiment
t = h.Vector().record(h._ref_t)

# initialize and run
h.finitialize(-65 * mV)
h.continuerun(100 * ms)

# plot
import matplotlib.pyplot as plt
plt.plot(t, cell0.v_soma)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()

