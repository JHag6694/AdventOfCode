#
import os

def log(text):
    print(text)

dataFile = os.getcwd()+"\\aoc2021-01.txt"
items = []
f = open(dataFile, "r")
for x in f:
    # log("line:".format(x))
    items.append(int(x))
f.close()

increaseCount = 0
for i in range(0+1, len(items)):
    if (items[i] > items[i-1]):
        increaseCount = increaseCount+1

log("increaseCount : {}".format(increaseCount))

# Stage 2 : 
slidingIncreaseCount = 0
for i in range(0+3, len(items)):
    sumA = items[i]+items[i-1]+items[i-2]
    sumPrev = items[i-1]+items[i-2]+items[i-3]
    if (sumA > sumPrev):
        slidingIncreaseCount = slidingIncreaseCount+1

log("slidingIncreaseCount : {}".format(slidingIncreaseCount))
