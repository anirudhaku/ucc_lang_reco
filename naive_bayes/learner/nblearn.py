__author__ = 'leo'

import sys
import string
import pickle

try:
    fHand = open(sys.argv[1], 'r', errors='ignore')
except:
    print ('File cannot be opened')
    exit()

# Read the training file and create dictionary.
counts = dict()
counts['labels'] = dict()
for line in fHand:
    for c in string.punctuation:
        line = line.replace(c, "")
    words = line.split()

    if words[0] not in counts['labels']:
        counts[words[0]] = dict()
        counts['labels'][words[0]] = 1
    else:
        counts['labels'][words[0]] += 1

    for word in words[1:]:
        if word not in counts[words[0]]:
            counts[words[0]][word] = 1
        else:
            counts[words[0]][word] += 1


#print(counts)
# Dump the training data into Model File for classifier to use.
pickle.dump(counts, open(sys.argv[2], 'wb'))
