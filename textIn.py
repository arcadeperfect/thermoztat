import numpy as np
import matplotlib.pyplot as plt

import json

path = 'textData/dadata.txt'

with open(path) as f:
    data = f.readlines()

parsed = []
print 'arse'
for i in data:
    z = eval(i)
    #print z[0],z[1],z[2]
    d = {'date':z[0],'time':z[1],'temp':z[2]}
    parsed.append(d)
    print i

ft = []
for i in parsed:

    if not 'nan' in i['temp']:
        #print type(i['temp'])
        try:
            ft.append(float(i['temp']))
        except:
            pass




jsonString = json.dumps(parsed, indent=4)

print jsonString
with open('jsonout.txt', 'w') as outfile:
    outfile.write(jsonString)


ar = np.asarray(ft)
y = np.linspace(0,len(ft),num=len(ft))
f = matPlot.sago(ar,111,3)





plt.plot(y,ft, 'x')
plt.plot(y,f, color = 'red')
plt.show()
