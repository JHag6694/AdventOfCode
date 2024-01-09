#
import os


def log(text):
    print(text)


file_path = os.getcwd() + "\\2022\\p02-input.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


# Stage 1 :
score = 0
for i in range(len(lines)):
    oppPlay = ord(lines[i][0]) - ord("A") + 1
    myPlay = ord(lines[i][-1]) - ord("X") + 1
    diff = (myPlay - oppPlay) % 3
    if diff == 0:
        res = 3
    elif diff == 1:
        res = 6
    else:
        res = 0
    score += myPlay + res

log("Score : {}".format(score))
