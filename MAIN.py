print('Uxugin Analyze 1.1.0')

import numpy
import scipy
import scipy.stats

fileName=input('File: ')
file=open(fileName, 'r')
data=file.read().split('\n')
file.close()
for i in range(len(data)):
    data[i]=float(data[i])
#print(data)
    
mean=numpy.mean(data)
print('Mean: '+str(mean))

median=numpy.median(data)
print('Median: '+str(median))

mode=scipy.stats.mode(data)
mode=mode.mode[0]
print('Mode: '+str(mode))

deviations=[]
for i in data:
    deviations.append(numpy.abs(i-mean))
mad=numpy.mean(deviations)
print('MAD: '+str(mad))

iqr=scipy.stats.iqr(data)
print('IQR: '+str(iqr))

std=numpy.std(data)
print('Standard Deviation: '+str(std))
