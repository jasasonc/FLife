import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')
import FLife
import numpy as np


dt = 1e-4
x = np.random.normal(scale=100, size=10000)

C = 1.8e+22
k = 7.3

# Spectral data
sd = FLife.SpectralData(input=x, dt=dt)

# Rainflow reference fatigue life
rf = FLife.Rainflow(sd)

# Spectral methods
dirlik = FLife.Dirlik(sd)
tb2 = FLife.TovoBenasciutti2(sd)
print(f'          Rainflow: {rf.get_life(C = C, k=k):4.0f} s')
print(f'            Dirlik: {dirlik.get_life(C = C, k=k):4.0f} s')
print(f'Tovo Benasciutti 2: {tb2.get_life(C = C, k=k):4.0f} s')