__author__ = 'leo'

import sys
import glob
import re

# Open Training File to write.
try:
    fHand = open(sys.argv[1], 'w')
except:
    print ('File cannot be opened')
    exit()

# Open directory containing all the training files.
files = sorted(glob.glob(sys.argv[2]))

for file in files:
    f=open(file, 'r', errors='ignore')
    fileName = file.split('/')[-1].split('.')[0]
    fHand.write(fileName + ' ')
    for line in f:
        fHand.write(line.strip() + ' ')
    fHand.write('\n')
    f.close()


