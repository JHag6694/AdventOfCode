#
import os
import logging

FORMAT = '%(asctime)s  %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('p03')
logger.setLevel(logging.INFO)


dataFile = os.getcwd()+"\\p03-input.txt"
items = []
f = open(dataFile, "r")
for x in f:
    logger.debug("line:%s", x)
    items.append(x.rstrip('\n'))
f.close()
logger.info("lines read:%d", len(items))

# 0001_1001_1011
dataGamma = 0
dataEpsilon = 0
for i in range(0, 12):
    count = [0, 0]
    for item in iter(items):
        count[int(item[i])] += 1
    if (count[0] > count[1]):
        dataGamma = 2*dataGamma
        dataEpsilon = 2*dataEpsilon+1
    else:
        dataGamma = 2*dataGamma+1
        dataEpsilon = 2*dataEpsilon
logger.info("Expected powerCons:3923414, found:%d", dataGamma*dataEpsilon)

# Part 2
currItems = items
nextItems = []
for i in range(0, 12):
    if (len(currItems) > 1):
        # Find most common value
        count = [0, 0]
        for item in iter(currItems):
            count[int(item[i])] += 1
        # Keep match
        logger.info("Iter %d : counts=%d,%d", i, count[0], count[1])
        for item in iter(currItems):
            test0 = (count[0] > count[1]) and (item[i] == "0")
            test1 = (count[1] >= count[0]) and (item[i] == "1")
            if (test0 or test1):
                nextItems.append(item)
        currItems = nextItems
        nextItems = []
OGR = eval('0b' + currItems[0])
logger.info("currItems %s : OGR=%d", currItems[0], OGR)

currItems = items
nextItems = []
for i in range(0, 12):
    if (len(currItems) > 1):
        # Find most common value
        count = [0, 0]
        for item in iter(currItems):
            count[int(item[i])] += 1
        # Keep match
        logger.info("Iter %d : counts=%d,%d", i, count[0], count[1])
        for item in iter(currItems):
            test0 = (count[0] <= count[1]) and (item[i] == "0")
            test1 = (count[1] < count[0]) and (item[i] == "1")
            if (test0 or test1):
                nextItems.append(item)
        currItems = nextItems
        nextItems = []
CSR = eval('0b' + currItems[0])
logger.info("currItems %s : CSR=%d", currItems[0], CSR)

logger.info("result expected:5852595, found=%d", CSR*OGR)
