import numpy as np
import matplotlib as mp
mp.use('Agg')

import matplotlib.pyplot as plt

count = 0

def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

with open("rawData") as f:
    content = f.readlines()

cdfVals = []
step = 0.1

for l in range(len(content)):
    avg = 0
    ping = 0
    if 'traceroute' in content[l]:
        words = content[l-1].split( )
        for x in words[1:]:
            if isFloat(x):
                avg += float(x)
                ping += 1
        val = avg/ping
        cdfVals.append(val)
    elif l == len(content)-1:
        words = content[l].split( )
        for x in words[1:]:
            if isFloat(x):
                avg += float(x)
                ping += 1
        val = avg/ping
        cdfVals.append(val)

plt.ylabel("Probability")
plt.xlabel("Ping Time (ms)")
plt.title("en.csme.gov.cn Ping Stats")

cdfVals = np.array(cdfVals).astype(np.float)
sortCdf = np.sort(cdfVals)
x = np.sort(cdfVals)
sortCdf /= (step*sortCdf).sum()

cy = np.cumsum(sortCdf*step)

plt.plot(x,cy,'b--')
plt.savefig("trace_cdf.png")
        
print len(cdfVals)

