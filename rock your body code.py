#Don't For get to run pip install rich on terminal. It will intall all important file to run it.

import sys
import time
from rich import print

def printLyrics():
    lines = [
        ("I wanna da-", 0.06, 0.4),
        ("I wanna dance in the lights", 0.05, 0.6),
        ("I wanna ro-", 0.07, 0.4),
        ("I wanna rock your body", 0.08, 0.8),
        ("I wanna go-", 0.08, 0.4),
        ("I wanna go for a ride", 0.06, 0.9),
        ("Hop in the music and", 0.07, 0.4),
        ("Rock your body", 0.08, 0.5),
        ("Rock that body", 0.07, 0.4),
        ("Come on, come on", 0.04, 0.3),
        ("Come on, come on", 0.05, 0.4),
        ("(Rock your body)", 0.03, 0.4),
        ("Rock that body", 0.05, 0.4),
        ("Come on, come on)", 0.04, 0.3),
        ("Rock that body", 0.08, 0.6),
    ]

    for text, char_delay, line_pause in lines:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()  # new line
        time.sleep(line_pause)

printLyrics()
