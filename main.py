"""Main file that records a Firefox page. Especially/originally made to record Zoom-lectures."""

import sys
from Webdriver import Webdriver
from utils import find_vacant_filename
from FFmpeg_util import FFmpeg_util

if len(sys.argv) !=  2:
    raise Exception("The script takess one command line argument: The url to record from.")


url = sys.argv[1] # Get url from terminal argument.

zoom = True if "zoom" in url else False # Zoom-recording True or False. 

open_webpage = Webdriver(url, zoom_recording = zoom).get_url().set_fullscreen()

minutes = int(sys.argv[1]) # Get minutes from terminal argument.

# Check if command line argument is integer. 
try:
    minutes += 1 
except TypeError:
    raise Exception("The minutes have to be an integer.")

# Reset the integer- 
minutes -= 1
    
filename = find_vacant_filename()

recorder = FFmpeg_util("/".join(path)+"/"+filename)

recorded = recorder.record_screen_with_audio(minutes = minutes) 

open_webpage.close_driver()

recorded.compress_file().delete_uncompressed_file()
