# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:25:40 2015

@author: Sarthf
"""

# NOR GATE ANN

import random as rnd

trainingSet = {(0,0):1,(1,0):0,(0,1):0,(1,1):0}
x0 = 1 # Bias
w0 = 1 # ""
w1 = rnd.random()
w2 = rnd.random()
r = 0.1
threshold = 1

for i in range(100): # Train it 100 times (could be lower)
    
    x1 = rnd.randint(0,1)
    x2 = rnd.randint(0,1)
    activation = x0*w0 + x1*w1 + x2*w2
    if (activation >= threshold):
        output = 1
    else:
        output = 0
    expected = trainingSet[(x1,x2)]
    error = expected - output
    w1 += r * error * x1
    w2 += r * error * x2

print "Done training, now test it."


for j in range(4): # Test It for each of the 4 input combinations
    x1 = int(input())
    x2 = int(input())
    activation = x0*w0 + x1*w1 + x2*w2
    if (activation >= threshold):
        output = 1
    else:
        output = 0
    print "Output: " + str(output)
    
    