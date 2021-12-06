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
log("lines read:{}".format(len(items)))

# 0001_1001_1011
dataGamma = 0
dataEpsilon = 0
dataGammaS = ""
dataEpsilonS = ""
for i in range(0, 12):
    count0 = 0
    count1 = 0
    for item in iter(items):
        if (item[i] == "0"):
            count0 = count0+1
        else:
            count1 = count1+1
    if (count0 > count1):
        dataGamma = 2*dataGamma
        dataEpsilon = 2*dataEpsilon+1
        dataGammaS += "0"
        dataEpsilonS += "1"
    else:
        dataGamma = 2*dataGamma+1
        dataEpsilon = 2*dataEpsilon
        dataGammaS += "1"
        dataEpsilonS += "0"
    log("loop#: {}".format(i))
    log("gamma: {}, {}".format(dataGamma, dataGammaS))
    log("epsilon: {}, {}".format(dataEpsilon, dataEpsilonS))
log("powerCons: {}".format(dataGamma*dataEpsilon))

# Part 2
currItems = items
nextItems = []
for i in range(0, 12):
    log("Iter {} : itemsLen={}".format(i, len(currItems)))
    if (len(currItems) > 1):
        # Find most common value
        count = [0, 0]
        for item in iter(currItems):
            if (item[i] == "0"):
                count[0] += 1
            else:
                count[1] += 1
        # Keep match
        log("Iter {} : counts={}".format(i, count))
        for item in iter(currItems):
            test0 = (count[0] > count[1]) and (item[i] == "0")
            test1 = (count[1] >= count[0]) and (item[i] == "1")
            if (test0 or test1):
                nextItems.append(item)
        currItems = nextItems
        nextItems = []
OGR = eval('0b' + currItems[0])
log("currItems={}, OGR={}".format(currItems[0], OGR))

currItems = items
nextItems = []
for i in range(0, 12):
    log("Iter {} : itemsLen={}".format(i, len(currItems)))
    if (len(currItems) > 1):
        # Find most common value
        count = [0, 0]
        for item in iter(currItems):
            if (item[i] == "0"):
                count[0] += 1
            else:
                count[1] += 1
        # Keep match
        log("Iter {} : counts={}".format(i, count))
        for item in iter(currItems):
            test0 = (count[0] <= count[1]) and (item[i] == "0")
            test1 = (count[1] < count[0]) and (item[i] == "1")
            if (test0 or test1):
                nextItems.append(item)
        currItems = nextItems
        nextItems = []
CSR = eval('0b' + currItems[0])
log("currItems={}, CSR={}".format(currItems[0], CSR))

log("result={}".format(CSR*OGR))
# result=5873028 : pas bon