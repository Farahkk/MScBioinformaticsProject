#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([2, 33, 5, 0, 1, 1, 5, 1, 0, 2, 3, 49, 40])
mylabels = ["Crossmab", "scFv", "Fab", "ScFab", "VHFc", "XscFv", "single-domain", "TNFSF10-fragment",
             "Pseudomonas aeruginosa Type III secretion protein PcrV", "Hinge", "VHH", "Fc", "Other"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Antibody Type: (Special Format Chains)")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()