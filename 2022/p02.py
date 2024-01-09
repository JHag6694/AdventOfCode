#
import os

def log(text):
    print(text)


file_path = os.getcwd() + "\\2022\\p02-input.txt"
items = []
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


# Stage 1 :
