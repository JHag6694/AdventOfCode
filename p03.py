#
import os

def log(text):
    print(text)

dataFile = os.getcwd()+"\\p03-input.txt"
items = []
f = open(dataFile, "r")
for x in f:
    # log("line:".format(x))
    items.append(x)
f.close()
log ("lines read:{}".format(len(items)))

#0001_1001_1011
dataGamma=0
dataEpsilon=0
dataGammaS=""
dataEpsilonS=""
for i in range(0, 12):
    count0=0
    count1=0
    for item in iter(items):
        if (item[i]=="0"):
            count0=count0+1
        else:
            count1=count1+1
    if (count0>count1):
        dataGamma=2*dataGamma
        dataEpsilon=2*dataEpsilon+1
        dataGammaS+="0"
        dataEpsilonS+="1"
    else:
        dataGamma=2*dataGamma+1
        dataEpsilon=2*dataEpsilon
        dataGammaS+="1"
        dataEpsilonS+="0"
    log("loop#: {}".format(i))    
    log("gamma: {}, {}".format(dataGamma, dataGammaS))
    log("epsilon: {}, {}".format(dataEpsilon, dataEpsilonS))



log("powerCons: {}".format(dataGamma*dataEpsilon))
