import sys

x_correct_range = [1, 10]
y_correct_range = [1, 10]

x_possible_range = [-sys.maxint, sys.maxint]
y_possible_range = [-sys.maxint, sys.maxint]


for i in range(20):
    x1 = int(raw_input("x1: "))
    y1 = int(raw_input("y1: "))
    if (x1 < x_possible_range[0] and x1 < x_correct_range[0]):
        x_possible_range[0] = x1
    if (x1 > x_possible_range[1] and x1 > x_correct_range[1]):
        x_possible_range[1] = x1
    if (y1 < y_possible_range[0] and y1 < y_correct_range[0]):
        y_possible_range[0] = y1
    if (y1 > y_possible_range[1] and y1 > y_correct_range[1]):
        y_possible_range[1] = y1

print x_correct_range
print y_correct_range
print x_possible_range
print y_possible_range
        
    
        
        
    

