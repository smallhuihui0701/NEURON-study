NEURON {
  POINT_PROCESS HalfGap
  POINTER vgap
  RANGE r, i
  ELECTRODE_CURRENT i
}

PARAMETER {r = 3 (megohm)}

ASSIGNED {
  v (millivolt)
  vgap (millivolt)
  i (nanoamp)
}

BREAKPOINT { i = (vgap - v) / r }
