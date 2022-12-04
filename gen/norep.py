#!/usr/bin/env python3

import numpy as np
from itertools import permutations

chords = permutations(range(0,12),4)
chords = np.array(list(chords),dtype=int)
chords = np.delete(chords, np.where(
    (chords[:,0]!=0)&(chords[:,1]!=0)&(chords[:,2]!=0)&(chords[:,3]!=0))[0], axis=0)

print(chords)

np.savetxt("../chords.csv",chords,delimiter=",")
