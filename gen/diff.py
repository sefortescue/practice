#!/usr/bin/env python3

import numpy as np

tot = pow(12,4)
diffs = np.empty([tot,4],dtype=int)

for i in range(tot):
    nextVal = i
    for j in range(3,-1,-1):
        currRem = nextVal % 12
        diffs[i][j] = currRem
        nextVal = nextVal // 12

np.savetxt("diffs.csv",diffs,delimiter=",")
