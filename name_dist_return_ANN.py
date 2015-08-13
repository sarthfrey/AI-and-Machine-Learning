from openpyxl import load_workbook

wb = load_workbook(filename='name_dist_return.xlsx')
ws = wb.active

w1 = 10
w2 = 10
threshhold = 30
r = -0.045
counterCorrect = 0
counterIncorrect = 0

for row in ws.rows:
    
    #preprocessing
    name = str(row[0].value)
    dist = row[1].value
    if (str(row[2].value) == 'M'):
        gender = 1
    elif (str(row[2].value) == 'F'):
        gender = 0
    if (str(row[3].value) == 'Y'):
        comeBack = 1
    elif (str(row[3].value) == 'N'):
        comeBack = 0
    #/preprocessing

    
    expected = comeBack        
    x1 = dist
    x2 = gender
    x1w1 = x1 * w1
    x2w2 = x2 * w2
    if (x1w1 + x2w2 < threshhold):
        output = 1
    else:
        output = 0
    error = expected - output
    if (error == 0):
        counterCorrect += 1
    else:
        counterIncorrect += 1
    print 'name is ' + name + '.'
    print 'x1 is ' + str(x1) + ' and x2 is ' + str(x2) + '.'
    print 'w1 is ' + str(w1) + ' and w2 is ' + str(w2) + '.'
    print 'x1w1 is ' + str(x1w1) + ' and x2w2 is ' + str(x2w2) + '.'
    print 'sum us ' + str(x1w1 + x2w2) + '.'
    print 'right/wrong: ' + str(float(counterCorrect)) + ' and ' + str(float(counterIncorrect)) + '.'
    print ''
    w1 = r * x1 * error + w1
    w2 = r * x2 * error + w2
    
    
    



