#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([42, 72, 69, 1, 0, 11])
mylabels = ["Conjugated", "Bispecific", "Fusion", "Conjugated Bispecific", 
            "Conjugated Fusion", "Bispecific Fusion"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Nature of the Antibody:")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()
