#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([267, 53])
mylabels = ["kappa", "lambda"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Light_Chain_Mutations")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()