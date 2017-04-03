import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

wFileName = "errorLog.txt"
wFile = open(wFileName, 'w')

with open("ping_data.txt") as f:
    content = f.readlines()

cdfVals = []
errors = []
step = 0.1
for line in content:
    if line[0] == '6':
        start = line.index("time=") + 5
        val = line[start:]
        end = val.index(" ");
        val = val[:end]
        cdfVals.append(val)
    else:
        errors.append(line)

plt.xlabel("Probability")
plt.ylabel("Ping Time (ms)")
cdfVals = np.array(cdfVals).astype(np.float)
sortCdf = np.sort(cdfVals)
x = np.sort(cdfVals)
sortCdf /= (step*sortCdf).sum()
cy = np.cumsum(sortCdf*step)

for i in cy[:10]:
    print i
print cy[86297]
#x = np.arange(min(sortCdf), max(sortCdf),step)
plt.plot(x,cy,'b--')
#n, bins, patch = plt.hist(sortCdf,bins=100,facecolor='purple',alpha=0.25,cumulative=True)

plt.savefig('cdf.png')

print len(cdfVals)
for error in errors:
    wFile.write(error)
    wFile.write("\n")
wFile.close()
