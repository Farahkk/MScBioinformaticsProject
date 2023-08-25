#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np      

y = np.array([0, 4, 1, 0, 5, 0, 3])
mylabels = ["cterclip", "deamination", "glycation","isomerisation", 
            "nterpca", "nterdeformylate", "oxidation"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Mutations: (Light Chain Confirmed PTM)")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()