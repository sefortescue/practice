#!/usr/bin/env python3

import numpy as np
from itertools import permutations

chords = permutations(range(0,12),4)
chords = np.array(list(chords),dtype=int)

np.savetxt("chords.csv",chords,delimiter=",")
