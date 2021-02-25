#!/usr/bin/python

import csv
import sys
import numpy as np
from matplotlib import pyplot as plt
import itertools

# V = IR, R = V / I, I = V / R

def parse_data(filename):
    data = np.genfromtxt(filename, delimiter=',',names=["x", "y"])

    #x = np.zeros(len(data))
    #y = np.zeros(len(data))
    #
    #inx = 0

    for i in data:
        #i['y'] = (5/1024) * i['x'] 
        #i['x'] = ((5/1024) * i['y']) * 10000
        i['x'] = 1024 - i['x']

    x = np.arange(len(data))

    np.sort(data)

    plt.plot(x,data['x'])
    plt.plot(data['x'], data['y'])
    plt.show()


if __name__ == '__main__':
    parse_data(sys.argv[1])
