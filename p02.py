#
import os

def log(text):
    print(text)


# __file__
# os.path.basename()
dataFile = os.getcwd()+"\\p02-input.txt"

f = open(dataFile, "r")

x_pos = 0
y_depth = 0
for line in f:
    items = line.split()
    if (items[0] == "forward"):
        x_pos = x_pos + int(items[1])
    elif (items[0] == "down"):
        y_depth = y_depth + int(items[1])
    elif (items[0] == "up"):
        y_depth = y_depth - int(items[1])
log("x_pos={}; depth={}; prod={}".format(x_pos, y_depth, x_pos*y_depth))
# Expected : 1762050

# Part 2
x_pos = 0
y_depth = 0
z_aim = 0
f.seek(0)
for line in f:
    items = line.split()
    if (items[0] == "forward"):
        x_pos = x_pos + int(items[1])
        y_depth = y_depth+z_aim*int(items[1])
    elif (items[0] == "down"):
        z_aim = z_aim + int(items[1])
    elif (items[0] == "up"):
        z_aim = z_aim - int(items[1])
log("x_pos={}; depth={}; prod={}".format(x_pos, y_depth, x_pos*y_depth))
# Expected : 1855892637

f.close()
