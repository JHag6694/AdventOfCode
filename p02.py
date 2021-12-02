#
import os


def log(text):
    print(text)


# __file__
# os.path.basename()
dataFile = os.getcwd()+"\\p02-input.txt"
items = []
f = open(dataFile, "r")
for x in f:
    items.append(x)
f.close()

x_pos = 0
y_depth = 0
for i, item in enumerate(items):
    if (item.startswith("forward")):
        x_pos = x_pos + int(item[7:])
    elif (item.startswith("down")):
        y_depth = y_depth + int(item[4:])
    elif (item.startswith("up")):
        y_depth = y_depth - int(item[2:])

log("x_pos={}; depth={}; prod={}".format(x_pos, y_depth, x_pos*y_depth))
