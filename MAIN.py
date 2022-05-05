VERSION='1.2.0'
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import numpy
import scipy
import scipy.stats

fileName=askopenfilename()
file=open(fileName, 'r')
data=file.read().split('\n')
file.close()
for i in range(len(data)):
    data[i]=float(data[i])
#print(data)

window=Tk()
window.title('Uxugin Analyze '+VERSION)
window.iconbitmap('Analyze.ico')

def showThing(text):
    Label(window, text=text).pack()
    
mean=numpy.mean(data)
showThing('Mean: '+str(mean))

median=numpy.median(data)
showThing('Median: '+str(median))

mode=scipy.stats.mode(data)
mode=mode.mode[0]
showThing('Mode: '+str(mode))

deviations=[]
for i in data:
    deviations.append(numpy.abs(i-mean))
mad=numpy.mean(deviations)
showThing('MAD: '+str(mad))

iqr=scipy.stats.iqr(data)
showThing('IQR: '+str(iqr))

std=numpy.std(data)
showThing('Standard Deviation: '+str(std))

mainloop()
