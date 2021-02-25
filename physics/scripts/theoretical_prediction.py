#!/usr/bin/python

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

r_prl = lambda r2, r3 : math.pow((1/r2 + 1/r3), -1)

v_out = lambda r1, r2, r3, vin : vin * (r_prl(r2,r3) / (r1 + r_prl(r2,r3)))

def generate_data(r1,r3,vin):
    x = np.arange(0,r1)
    y = np.zeros(r1)
  
    for i in range(1, r1):
        y[i] = (5 * i*r3) / ((r1-i)*(i+r3) + i*r3)
        #y[i] = v_out((r1 - i),i,r3,vin)

    return x,y

if __name__ == "__main__":
    x,y = generate_data(50000, int(sys.argv[1]), 5)

    plt.plot(x,y)
    plt.xlabel('R2 [ohms]')
    plt.ylabel('ouptut voltage [V]')
    plt.title(sys.argv[2])
    plt.show()
