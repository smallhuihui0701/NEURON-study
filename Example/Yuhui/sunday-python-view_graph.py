from neuron import h
from neuron.units import um
import plotly

class Cell:
    def __init__(self):
        main = h.Section(name="main", cell=self)
        dend1 = h.Section(name="dend1", cell=self)
        dend2 = h.Section(name="dend2", cell=self)

        dend1.connect(main)
        dend2.connect(main)

        main.diam = 10 * um
        dend1.diam = 2 * um
        dend2.diam = 2 * um

        self.main = main 
        self.dend1 = dend1 
        self.dend2 = dend2
        self.all = main.wholetree()

from matplotlib import pyplot
my_cell = Cell()
ps = h.PlotShape(False)
ps.variable("v")
ps.plot(pyplot)
h.topology()
pyplot.show()