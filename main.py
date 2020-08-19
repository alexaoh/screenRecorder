"""Main file that records a Firefox page. Especially/originally made to record Zoom-lectures."""

import sys
from Webdriver import Webdriver
from utils import find_vacant_filename
from FFmpeg_util import FFmpeg_util

if len(sys.argv) !=  2:
    raise Exception("The script takes one command line argument: The url to record from.")


url = sys.argv[1] # Get url from terminal argument.

zoom = True if "zoom" in url else False # Zoom-recording True or False. 

open_webpage = Webdriver(url, zoom_recording = zoom).get_url().set_fullscreen()

filename = find_vacant_filename()

recorder = FFmpeg_util(filename)

recorded = recorder.record_screen_with_audio(minutes = 0.5) 

open_webpage.close_driver()

recorded.compress_file().delete_uncompressed_file()
