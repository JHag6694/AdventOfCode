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
for i in range(1, len(items)):
    if (items[i] > items[i-1]):
        increaseCount=increaseCount+1

log("Increase number : {}".format(increaseCount))
