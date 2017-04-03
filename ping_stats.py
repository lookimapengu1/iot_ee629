import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

with open("ping_data.txt") as f:
    content = f.readlines()

cdfVals = []
errors = []

for line in content[:100]:
    if line[0] == '6':
        start = line.index("time=") + 5
        val = line[start:]
        end = val.index(" ");
        val = val[:end]
        cdfVals.append(val)
    else:
        errors.append(line)

num_bins = 20
fig = plt.figure()
ax = fig.add_subplot(111)
cdfVals = np.array(cdfVals).astype(np.float)

sortCdf = np.sort(cdfVals)
    
n, bins, patch = plt.hist(sortCdf,bins=20,normed=True,facecolor='blue',alpha=0.5)

plt.savefig('cdf.png')

print len(cdfVals)
for error in errors:
    print error
