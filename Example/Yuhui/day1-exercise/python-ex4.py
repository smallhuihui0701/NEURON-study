from neuron import h
from neuron.units import mV, ms, µm
import plotnine as p9
import pandas as pd
import sys
h.load_file("stdrun.hoc")

# check if HalfGap has been compiled
try:
    h.HalfGap
except AttributeError:
    print("HalfGap.mod file not compiled. Run nrnivmodl in the terminal.")
    sys.exit(-1)

class YNeuron:
    def __init__(self):
        self.main = h.Section('main')
        self.branch1 = h.Section('branch1')
        self.branch2 = h.Section('branch2')
        self.branch1.connect(self.main)
        self.branch2.connect(self.main)
        for sec in self.main.wholetree():
            sec.L = 100 * µm
            sec.diam = 1 * µm
            sec.insert(h.hh)
            sec.nseg = 33

        self.v = h.Vector().record(self.main(0.5)._ref_v)

cell1 = YNeuron()
cell2 = YNeuron()

stim = h.IClamp(cell1.main(0.5))
stim.delay = 5 * ms
stim.dur = 0.2 * ms
stim.amp = 1  # nA

t = h.Vector().record(h._ref_t)

# initialize and run
h.finitialize(-65 * mV)
h.continuerun(25 * ms)

# plot the results
def do_plot(title):
    data = pd.DataFrame({
        't': t,
        'cell1': cell1.v,
        'cell2': cell2.v,
    }).melt(id_vars='t', var_name='cell (main sec)', value_name='v (mV)')


    (
        p9.ggplot(data, p9.aes(x='t', y='v (mV)', color='cell (main sec)'))
        + p9.geom_line(size=2)
        + p9.ggtitle(title)
    ).show()

do_plot("First experiment: cells not connected")

#
# second experiment: connect the cells with HalfGap
#
halfgap1 = h.HalfGap(cell1.branch1(1))
halfgap2 = h.HalfGap(cell2.branch1(1))

halfgap1._ref_vgap = cell2.branch1(1)._ref_v
halfgap2._ref_vgap = cell1.branch1(1)._ref_v

# initialize and run
h.finitialize(-65 * mV)
h.continuerun(25 * ms)

# plot the results
do_plot("Second experiment: cells connected with HalfGap")

