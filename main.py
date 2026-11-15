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

# TUI
import questionary
import rich

def main():
    if mode == "r":
        print("You are in Random mode!\n")

        # randomizes everything
        names = "John"
        time = 0.00
        gravity = 1.00
        temperature = 27

    elif mode == "j":
        print("You are in JSON mode!\n")

        # reads everything and assigns it a variable
        names = data["astronauts"]
        time = [data["start"], data["end"]]
        gravity = data["gravity"]
        temperature = data["temperature_c"]

    print(f"Astronauts: {names}\n") #placeholder

def check():

    print("\nPerforming checks...\n")

    # gravity


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





