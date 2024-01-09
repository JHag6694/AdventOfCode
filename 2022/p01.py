#
import os

def log(text):
    print(text)

file_path = os.getcwd()+"\\2022\\p01-input.txt"
items = []
with open(file_path, 'r') as file:
    items = [line.strip() for line in file.readlines()]

curCalInd = 1
curCal = 0
maxCalInd = 0
maxCal = 0
for i in range(0+1, len(items)):
    if (items[i] == ""): 
        log ("CalInd : {}, Cal : {}".format(curCalInd, curCal))
        if (curCal > maxCal):
            maxCal=curCal
            maxCalInd=curCalInd
        curCalInd+=1    
        curCal = 0
    else:
        curCal+=int(items[i])
if (curCal > maxCal):
    maxCal=curCal
    maxCalInd=curCalInd
    
log ("CalInd : {}, Cal : {}".format(maxCalInd, maxCal))

