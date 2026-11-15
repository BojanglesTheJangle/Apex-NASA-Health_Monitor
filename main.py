# Made by BojanglesTheJangle for the 2026 NASA Space Apps Challenge

# Data & command line argument
import json
import pathlib
import sys

# Understanding time
import datetime

# Math and statistical calculations
import random
import statistics

def main():
    if mode == "r":
        print("You are in Random mode!\n")
        name = "John"
    elif mode == "j":
        print("You are in JSON mode!\n")
        name = data["astronauts"]

    print(f"Astronauts: {name}\n")

# checks for argument, sets mode. if no argument (or no j found), set mode to random
# r = random mode, j = json mode
if len(sys.argv) > 1 and sys.argv[1] == "j":
    mode = sys.argv[1]
    # json file
    link = input("What is the file name of your JSON file? (do not add the extention, .json; default is artemis.): \n")

    # opens json
    with open(link + ".json", "r") as file:
        data = json.load(file)

else:
    mode = "r"

main()





