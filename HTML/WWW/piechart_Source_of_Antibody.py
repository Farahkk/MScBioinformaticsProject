#!/usr/bin/python3
#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([2, 4, 28, 2, 523, 277, 3, 9, 1, 2, 3])
mylabels = ["Canine", "Caninized", "Chimeric", "Fenilized", "Human", "Humanized", 
            "Llama", "Mouse", "Murine", "Rat", "Resurfaced"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Source of the Antibody:")
plt.show() 

#Two lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()
