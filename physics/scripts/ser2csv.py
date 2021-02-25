#!/usr/bin/python

import sys
import serial 

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=None)

def read_data_to_csv(f):
    s = ser.readline()
    print(s)
    f.write(s.decode('utf-8'))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: ser2csv <output filename> \n \
                default settings: \n\
                * port: /dev/ttyACM0 \n\
                * baud rate: 115200 \n\
                * timeout: None\n\
                \rterminate with CTRL+C')
        exit()

    f = open(sys.argv[1], 'w+')
    while 1:
        read_data_to_csv(f)
