#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([306, 298, 1, 0])
mylabels = ["potential N-linked glycosylation sites", "confirmed N-linked glycosylation sites",
             "potential O-linked glycosylation sites", "confirmed O-linked glycosylation sites"]

plt.pie(y, labels = mylabels)
plt.legend(title = "PTMs: (Heavy Chain Mutations)")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()