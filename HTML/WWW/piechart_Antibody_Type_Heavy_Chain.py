#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([335, 31, 2, 118, 37])
mylabels = ["IgG1", "IgG2", "IgG3", "IgG4", "Fv"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Antibody Type: (Special Format Chains)")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()