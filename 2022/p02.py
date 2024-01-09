#
import os


def log(text):
    print(text)


file_path = os.getcwd() + "\\2022\\p02-input.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Rock : 1, Paper : 2, Scissors : 3
# Stage 1 :
score = 0
for i in range(len(lines)):
    oppPlay = ord(lines[i][0]) - ord("A") + 1  # 1, 2, 3
    myPlay = ord(lines[i][-1]) - ord("X") + 1  # 1, 2, 3
    res = (myPlay - oppPlay + 1) % 3  # 0 lost, 1 :draw, 2: won
    score = score + myPlay + (res * 3)

log("Score1 : {}".format(score))  # 13924

# Stage 2 :
score2 = 0
for i in range(len(lines)):
    oppPlay = ord(lines[i][0]) - ord("A") + 1  # 1, 2 or 3
    res = ord(lines[i][-1]) - ord("X")  # 0:lost 1:draw 2:won
    myPlay = ((oppPlay + res - 1) - 1) % 3 + 1
    score2 += myPlay + (res * 3)

log("Score2 : {}".format(score2))
