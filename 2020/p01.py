#
import os


def log(text):
    print(text)


dataFile = os.getcwd()+"\\2020\\p01-input.txt"
items = []
f = open(dataFile, "r")
for x in f:
    # log("line:".format(x))
    items.append(int(x))
f.close()

for i in range(0, len(items)):
    for j in range(i+1, len(items)):
        sum = items[i]+items[j]
        #log("Sum({0}, {1})={2}".format(i, j, sum))
        if (sum == 2020):
            prod = items[i]*items[j]
            log("Found : Index=(i={}, j={}); values={},{}; Prod={}"
                .format(i, j, items[i], items[j], prod))
