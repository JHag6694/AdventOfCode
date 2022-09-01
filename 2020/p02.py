#
import os
import logging
import re

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S'
                    )

dataFile = os.getcwd()+"\\2020\p02-input.txt"
items = []
f = open(dataFile, "r")
for x in f:
    logging.debug("line:%s", x)
    items.append(x.rstrip('\n'))
f.close()
logging.info("lines read:%d", len(items))

totalP1=0
totalP2=0
for item in iter(items):
   result = re.search(r"([0-9]+)-([0-9]+) (.): ([a-z]+)", item)
   if (result == None):
      logging.warn ("No match !?")
   else:
      min=int(result.group(1))
      max=int(result.group(2))
      letter=result.group(3)
      data=result.group(4)
      count=data.count(letter)
      if (min <= count) and (count <= max):
         totalP1=totalP1 +1
      if ((data[min-1]==letter) ^ (data[max-1]==letter)):
         totalP2=totalP2 +1
logging.info("resultP1=%d", totalP1)
logging.info("resultP2=%d", totalP2)
