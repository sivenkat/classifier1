# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.spatial import distance

#inFile = np.genfromtxt("playoffData2007-2014.csv")
inFile = open("playoffData2007-2014.csv")

numLines = 0
outputList = []
inFileLines = inFile.readlines()
inFile.close()
for line in inFileLines:
    numLines += 1
   # readLine = inFile.readline()
   # print(inFile.readline())
    outputList.append(line.strip().split(","))

numCol = len(outputList[0])

mainArray = np.array(outputList)

testFile = open("2015playoffTeamsData.csv")
test = testFile.readlines()
testFile.close()
testList = []
for line in test:
    testList.append(line.strip().split(","))

testArray = np.array(testList)

def KNNclassifier(training, test, k = 1, metric = 'euclidean'):
    '''Takes in a training array and a test array. Function finds the k
    closest observations in the training array for each observation in the
    test array and uses that to label the test observation'''
    
    training = training[1:,:]
    
    trainingData = training[:,2:]
    
    testData = test[:,2:]
    #create an array with distances
    distanceMatrix = distance.cdist(trainingData, testData, metric)
    #sort by column so the first row contains the smallest distances 
    #for each test observation
    sortedDistanceIndex = np.argsort(distanceMatrix, 0)
  
    #get the labels from the training set for the k number of test values
    labeledIndexesTeam = training[sortedDistanceIndex[0:k], 0]
    labeledIndexesYear = training[sortedDistanceIndex[0:k],1]
    
    print(labeledIndexesTeam)
    print(labeledIndexesYear)
 
    
    
