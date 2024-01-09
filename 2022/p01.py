#
import os


def log(text):
    print(text)


file_path = os.getcwd() + "\\2022\\p01-input.txt"
items = []
with open(file_path, "r") as file:
    for line in file.readlines():
        if line.strip() == "":
            items.append(0)
        else:
            items.append(int(line.strip()))
items.append(0)

# Stage 1 :
curCalInd = 1
curCal = 0
maxCalInd = 0
maxCal = 0
for i in range(0 + 1, len(items)):
    if items[i] == 0:
        log("CalInd : {}, Cal : {}".format(curCalInd, curCal))
        if curCal > maxCal:
            maxCal = curCal
            maxCalInd = curCalInd
        curCalInd += 1
        curCal = 0
    else:
        curCal += items[i]
log("CalInd : {}, Cal : {}".format(maxCalInd, maxCal))

# Stage 2 :
allCals = []
curCal = 0
for i in range(0 + 1, len(items)):
    if items[i] == 0:
        allCals.append(curCal)
        curCal = 0
    else:
        curCal += items[i]

max3cals = 0
for i in range(0, 3):
    curMax = max(allCals)
    max_index = allCals.index(curMax)
    log("Max{} : {}, {}".format(i, max_index, allCals[max_index]))
    del allCals[max_index]
    max3cals += curMax
log("max3cals : {}".format(max3cals))
