__author__ = 'leo'

import sys
import string
import pickle
import math

# Reading the Model File.
counts = pickle.load(open(sys.argv[1], 'rb'))
msgCount = sum(counts['labels'].values())

# No of words in each label.
wordCount = dict()
for label in counts['labels']:
    wordCount[label] = sum(counts[label].values())

# Vocabulary size.
uniqueWordVocab = dict()
vocabSize = 0
for label in counts['labels']:
    for item in counts[label]:
        if item not in uniqueWordVocab:
            uniqueWordVocab[item] = 1
vocabSize = sum(uniqueWordVocab.values())

# Finding the log of class probability.
classProb = dict()
for label in counts['labels']:
    classProb[label] = math.log(counts['labels'][label] / msgCount)

# Check whether add-one smoothing is required or not.
def smoothing(tempWords, label, tempword=None):
    addSmoothing = False
    for tempWord in tempWords:
        if tempword not in counts[label]:
            addSmoothing = True
            return addSmoothing
    return addSmoothing

# Open Test File.
try:
    fHand = open(sys.argv[2], 'r', errors='ignore')
except:
    print ('File cannot be opened')
    exit()

for line in fHand:
    for c in string.punctuation:
        line = line.replace(c, "")
    words = line.split()

    # Calculate the log of probability of each word in each label and store in the langClassify dictionary.
    sumProb = 0
    langClassify = dict()
    for label in counts['labels']:
        #doSmoothing = smoothing(words, label)
        #print(doSmoothing)
        #if (doSmoothing):
        sumProb = 0
        for word in words:
            if word in counts[label]:
                sumProb += math.log((counts[label][word] + 1) / (wordCount[label] + vocabSize + 1))
            else:
                sumProb += math.log(1 / (wordCount[label] + vocabSize + 1))
        #else:
        #    sumProb = 0
        #    for word in words:
        #        sumProb += math.log((counts[label][word]) / (wordCount[label]))

        langClassify[label] = classProb[label] + sumProb
        #print(langClassify[label])

    print(words[0])
    for label in counts['labels']:
        print(label)
        print(langClassify[label])


    classify = max(langClassify, key=langClassify.get)
    print(words[0] + "    " + classify + "\n---------------------")
