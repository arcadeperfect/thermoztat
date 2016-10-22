import matplotlib.pyplot  as plt
import matplotlib.dates as mdates
from timeDateTest import *
from matPlot import *
import numpy as np
path = './textData/dadata.txt'

with open(path) as f:
    data = f.readlines()

parsed = []

for i in data:
    z = eval(i)
    #print z[0],z[1],z[2]
    d = {'date':z[0],'time':z[1],'temp':z[2]}
    parsed.append(d)

datez = []

for i in parsed:
    if not 'nan' in i['temp']:
        if len(i['temp']) == 2:

            s = '%s %s' %(i['date'],i['time'])
            d = i['date']
            t = i['time']
            datez.append([stringToDatetime(d,t),i["temp"]])

#for i in datez:
#    print i


x = [i[0] for i in datez]
y = [int(i[1]) for i in datez]
y2 = sago(np.asarray(y),111,3)
print y2


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.plot(x,y2, color='red')
plt.gcf().autofmt_xdate()
plt.show()
