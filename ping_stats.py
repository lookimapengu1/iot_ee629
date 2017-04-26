#note: this script saves the graph instead of showing it because i'm running it headlessly on a raspberry pi so i can't see the graph.

#import all the libraries
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

#initialize the error file
wFileName = "errorLog.txt"
wFile = open(wFileName, 'w')

#read the data from the text file
with open("rawData") as f:
    content = f.readlines()

#initialize labels
cdfVals = []
errors = []
step = 0.1

#read in the file and sanitize data
for line in content:
    if line[0] == '6':
        start = line.index("time=") + 5
        val = line[start:]
        end = val.index(" ");
        val = val[:end]
        cdfVals.append(val)
    else:
        errors.append(line)

#set axes labels
plt.ylabel("Probability")
plt.xlabel("Ping Time (ms)")
plt.title("Battle.net Ping Times")
#convert strings to floats for calculations
cdfVals = np.array(cdfVals).astype(np.float)
#sort values
sortCdf = np.sort(cdfVals)
x = np.sort(cdfVals)
#normalize values for pdf
sortCdf /= (step*sortCdf).sum()
#get cumulative values
cy = np.cumsum(sortCdf*step)

#create plot
plt.plot(x,cy,'b--')

#save as a png
plt.savefig('cdf.png')

#if any errors were found, log them here
for error in errors:
    wFile.write(error)
    wFile.write("\n")
wFile.close()
