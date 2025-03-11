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
        dend.insert(h.hh)
        dend.connect(soma)
        self.soma = soma
        self.dend = dend
    def __repr__(self):
        return f'BallAndStick[{self._gid}]'

cell0 = BallAndStick(0)
cell1 = BallAndStick(1)

