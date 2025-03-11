from neuron import h
from neuron.units import mV, ms, µm
import plotnine as p9
import pandas as pd
h.load_file("stdrun.hoc")

class MyNeuron:
    def __init__(self):
        self.soma = h.Section('soma')
        self.soma.L = self.soma.diam = 10 * µm
        self.soma.insert(h.hh)
        self.esyn = h.ExpSyn(self.soma(0.5))
        self.esyn.tau = 2 * ms
        self.esyn.e = 0 * mV
        self.vtrace = h.Vector().record(self.soma(0.5)._ref_v)

# construct the cells
cell1 = MyNeuron()
cell2 = MyNeuron()

# setup the initial experiment: two stimuli
ns1 = h.NetStim()
ns1.number = 1
ns1.start = 5
nc1 = h.NetCon(ns1, cell1.esyn)
nc1.weight[0] = 0.001
nc1.delay = 0 * ms

ns2 = h.NetStim()
ns2.number = 1
ns2.start = 10
nc2 = h.NetCon(ns2, cell2.esyn)
nc2.weight[0] = 0.001
nc2.delay = 0 * ms

# setup recording (cells already record)
t = h.Vector().record(h._ref_t)

# initialize and run
h.finitialize(-65 * mV)
h.continuerun(20 * ms)

# plot the results
def do_plot(title):
    data = pd.DataFrame({
        't': t,
        'cell1': cell1.vtrace,
        'cell2': cell2.vtrace,
    }).melt(id_vars='t', var_name='cell', value_name='v (mV)')


    (
        p9.ggplot(data, p9.aes(x='t', y='v (mV)', color='cell'))
        + p9.geom_line(size=2)
        + p9.ggtitle(title)
    ).show()

do_plot("First experiment: cells not connected")

#
# second experiment: connect the cells
#
isyn = h.ExpSyn(cell2.soma(0.5))
isyn.tau = 4 * ms
isyn.e = -75 * mV
nc3 = h.NetCon(cell1.soma(0.5)._ref_v, isyn, sec=cell1.soma)
nc3.weight[0] = 0.005
nc3.delay = 1 * ms

# initialize and run
h.finitialize(-65 * mV)
h.continuerun(20 * ms)

# plot it
do_plot("Second experiment: cells connected with inhibition")