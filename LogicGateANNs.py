# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:56:02 2015

@author: Sarth
"""

import random

w1 = random.random()
w2 = random.random()
r = -0.15
for i in range(30):
    print ''
    print 'w1 is ' + str(w1) + ' and w2 is ' + str(w2)
    i1 = random.randint(0,1)
    i2 = random.randint(0,1)
    print ''
    print 'i1 is ' + str(i1) + ' and i2 is ' + str(i2)
    i1w1 = i1 * w1
    i2w2 = i2 * w2
    output = i1w1 + i2w2
    if(output < 1):
        output = 1
    else:
        output = 0
    print ''
    print 'output: ' + str(output)
    answ = int(input('expected: '))
    error = answ - output
    w1 = r * error * i1 + w1
    w2 = r * error * i2 + w2
print 'w1 is ' + str(w1) + ' and w2 is ' + str(w2)
while(True):
    i1 = int(input('i1: '))
    i2 = int(input('i2: '))
    i1w1 = i1 * w1
    i2w2 = i2 * w2
    output = i1w1 + i2w2
    if(output < 1):
        output = 1
    else:
        output = 0
    print ''
    print 'output: ' + str(output)

