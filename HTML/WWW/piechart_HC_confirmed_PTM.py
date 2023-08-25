#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np      

y = np.array([0, 49, 0, 0, 0, 0, 0, 10, 4, 1, 0])
mylabels = ["amidation", "cterclip", "deamination", "glycation", "hydroxylation",
            "isomerisation", "nterdeformylate", "nterpca",
            "oxidation", "succinide-formation", "succinimide-formation"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Mutations: (Heavy Chain Confirmed PTM)")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()