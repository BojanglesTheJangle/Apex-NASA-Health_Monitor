# Made by BojanglesTheJangle for the 2026 NASA Space Apps Challenge

# Data & command line argument
import json
import sys

# Understanding time
import datetime

# Math and statistical calculations
import random

# TUI
import questionary
from questionary import Style, Choice
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
# from rich import print

# style
custom_style = Style.from_dict({  
    "safe": "fg:#00ff00 bold",  # green
    "warning": "fg:#ffff00 bold",   # yellow
    "danger": "fg:#ff0000 bold", # red
})


def check(gravity, start, end, temperature, humidity, rad_dose, comms, mental):

    print("\nPerforming checks...\n")

    # days
    d_duration = (end - start).total_seconds() / 86400.0
    # months
    m_duration = d_duration/30.44

    # gravity

    gravity_status = "WARNING"
    bone_loss = None

    if gravity == 0.0:
        bone_loss = 0.8 * m_duration
    elif gravity > 0.0 and gravity < 1.0:
        gravity_status = "WARNING" # cannot accurately calculate
    elif gravity == 1.0:
        gravity_status = "NORMAL" # earth's gravity.
    else:
        gravity_status = "WARNING" # cannot accurately measure above 1.0, so warning will be sent.

    # temp & humidity

    temp_status = "WARNING"
    humidity_status = "WARNING"

    temp_reason="Just right."
    humidity_reason="Just right."

    if temperature < 18:
        temp_status = "WARNING"
        temp_reason = "Too cold."
    elif temperature < 27 and temperature > 18:
        temp_status = "NORMAL"
        temp_reason = "Just right."
    else:
        temp_status = "WARNING"
        temp_reason = "Too hot."

    if humidity < 30: 
        humidity_status = "WARNING"
        humidity_reason = "Too dry."
    elif humidity > 30 and humidity < 60:
        humidity_status = "NORMAL"
        humidity_reason = "Just right."
    else:
        humidity_status = "WARNING"
        humidity_reason = "Too moist."

    # radiation.

    total_rad = rad_dose * d_duration

    rad_status = "NORMAL"

    if rad_dose < 0.9:
        rad_status = "NORMAL"
    else:
        rad_status = "WARNING"

    if total_rad > 300:
        rad_status = "WARNING" # not really accurate.

    # communications

    comm_status = "NORMAL"

    if comms == False:
        comm_status = "DANGEROUS"

    # mental health

    mental_status = "NORMAL"

    if mental == False:
        mental_status = "WARNING"


    return gravity_status, temp_status, humidity_status, rad_status, comm_status, mental_status, bone_loss, temp_reason, humidity_reason, total_rad

        
    
def color_handle(gravity_result, temperature_result, humidity_result, rad_result, comm_result, mental_result):

    if gravity_result == "NORMAL":
        color = "class:safe"
    elif gravity_result == "WARNING":
        color = "class:warning"
    else:
        color = "class:danger"

    if temperature_result == "NORMAL":
        temp_color = "class:safe"
    elif temperature_result == "WARNING":
        temp_color = "class:warning"
    else:
        temp_color = "class:danger"

    if humidity_result == "NORMAL":
        humid_color = "class:safe"
    elif humidity_result == "WARNING":
        humid_color = "class:warning"
    else:
        humid_color = "class:danger"
   
    if rad_result == "NORMAL":
        rad_color = "class:safe"
    elif rad_result == "WARNING":
        rad_color = "class:warning"
    else:
        rad_color = "class:danger"

    if comm_result == "NORMAL":
        comm_color = "class:safe"
    else:
        comm_color = "class:danger"

    if mental_result == "NORMAL":
        mental_color = "class:safe"
    else:
        mental_color = "class:danger"

    return color, temp_color, humid_color, rad_color, comm_color, mental_color



def main():

    while True:

        print("\033[2J\033[H", end="")

        if mode == "r":
            print("You are in Random mode!\n")

            # randomizes everything (placeholder)
            
            gravity = 1.00
            temperature = 27

        elif mode == "j":
            print("You are in JSON mode!\n")

            # reads everything and assigns it a variable
            start = data["start"]
            end = data["end"]
        
            # converts to datetime objects
            start = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
            end = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))

            # defines variables
            gravity = data["gravity_g"]
            temperature = data["temperature_c"]
            humidity = data["humidity"]
            rad_dose = data["msv/day"]
            comms = data["comm_access"]
            mental = data["mental_health"]

            gravity_result, temp_result, humidity_result, rad_result, comm_result, mental_result, bone_loss, temp_reason, humidity_reason, total_rad = check(gravity, start, end , temperature, humidity, rad_dose, comms, mental)

            # changes color depending on class
            color, temp_color, humid_color, rad_color, comm_color, mental_color = color_handle(gravity_result, temp_result, humidity_result, rad_result, comm_result, mental_result)
        
            selected = questionary.select(
                "Dashboard",
                choices=[
                    Choice(
                        title=FormattedText([
                            (color, "Gravity: " + gravity_result),
                        ]),
                        value="gravity"
                    ),
                    Choice(
                        title=FormattedText([
                        (temp_color, "Temperature: " + temp_result) 
                        ]),
                        value="temperature"
                    ),
                    Choice(
                        title=FormattedText([
                            (humid_color, "Humidity: " + humidity_result)
                        ]),
                        value="humidity"
                    ),
                    Choice(
                        title=FormattedText([
                            (rad_color, "Radiation: " + rad_result)
                        ]),
                        value="radiation"
                    ),
                    Choice(
                        title=FormattedText([
                            (comm_color, "Communications: " + comm_result)
                        ]),
                        value="communication"
                    ),
                    Choice(
                        title=FormattedText([
                            (mental_color, "Mental Health: " + mental_result)
                        ]),
                        value="mental"
                    ),
                    Choice(
                        title=FormattedText([
                            ("class:danger", "Exit?")
                        ]),
                        value="exit"
                    )
                ],
                style=custom_style
            ).ask()


            # Selection, class safe, warning, and dangerous is now only used for colors.
            if selected == "gravity":

                print_formatted_text(FormattedText([
                    ("class:safe", f"\nGravity (1g=earth): {gravity}")
                ]),
                style=custom_style
                )

                if bone_loss is not None:
                    print_formatted_text(FormattedText([
                        ("class:safe", f"Bone loss: {bone_loss}%")
                    ]),
                    style=custom_style
                    )
                else:
                    print_formatted_text(FormattedText([
                        ("class:warning", "Bone loss estimate unavailable for this gravity level.")
                    ]),
                    style=custom_style
                    )
                print_formatted_text(FormattedText([
                    ("class:danger", "\n\n Warning... This information is not accurate, please be advised.\n")
                ]),
                    style=custom_style
                )
                questionary.press_any_key_to_continue().ask()

            if selected == "temperature":
                print_formatted_text(FormattedText([
                    ("class:safe", f"\nTemperature: {temperature}C")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                    ("class:warning", f"Overall: {temp_reason}")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                        ("class:danger", "\n\n Warning... This information is not accurate, please be advised.\n")
                    ]),
                    style=custom_style
                    )
                questionary.press_any_key_to_continue().ask()
            
            if selected == "humidity":
                print_formatted_text(FormattedText([
                    ("class:safe", f"\nHumidity: {humidity}%")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                    ("class:warning", f"Overall: {humidity_reason}")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                    ("class:danger", "\n\n Warning... This information is not accurate, please be advised.\n")
                ]),
                style=custom_style
                )
                questionary.press_any_key_to_continue().ask()

            if selected == "radiation":
                print_formatted_text(FormattedText([
                    ("class:safe", f"\nRadiation : {rad_dose}mSv/day")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                    ("class:warning", f"Total Radiation: {total_rad}")
                ]),
                style=custom_style
                )
                print_formatted_text(FormattedText([
                    ("class:danger", "\n\n Warning... This information is not accurate, please be advised.\n")
                ]),
                style=custom_style
                )
                questionary.press_any_key_to_continue().ask()

            if selected == "communication":
                print_formatted_text(FormattedText([
                    ("class:safe", f"\nAccess to communication: {comms}")
                ]),
                style=custom_style
                )
                questionary.press_any_key_to_continue().ask()
            if selected == "mental":
                print_formatted_text(FormattedText([
                    ("class:safe", f"\nDoing well: {comms}")
                ]),
                style=custom_style
                )
                questionary.press_any_key_to_continue().ask()
            if selected == "exit":
                print("\033[2J\033[H", end="")
                print("\nBye!\n")
                break


# checks for argument, sets mode. if no argument (or no j found), set mode to random
# r = random mode, j = json mode
if len(sys.argv) > 1 and sys.argv[1] == "j":
    mode = sys.argv[1]
    # json file
    link = input("What is the file name of your JSON file? (do not add the extention, .json; default is artemis.): \n")

    if not link:
        print("\n Error: No file found, defaulting to Artemis.json.")
        link = "artemis"

    # opens json
    with open(link + ".json", "r") as file:
        data = json.load(file)

else:
    mode = "r"

main() 