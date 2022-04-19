import numpy
data=[1, 2, 3, 4, 5]
mean=numpy.mean(data)
deviations=[]
for i in data:
    deviations.append(numpy.abs(i-mean))
mad=numpy.mean(deviations)
print(mad)
