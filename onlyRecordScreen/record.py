"""File for recording the screen with FFmpeg."""

import sys
# The path to the partent directory is added to be able to import from it below.
path = sys.path[0].split("/")
sys.path.append("/".join(path[:-1])+"/")

from utils import find_vacant_filename
from FFmpeg_util import FFmpeg_util

if len(sys.argv) != 2:
    raise Exception("The script takes one command line argument: The minutes to record for")

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

# Record for 'minutes' minutes to be sure that the entire lecture is recorded. 
recorded = recorder.record_screen_with_audio(minutes = minutes) 

recorded.compress_file().delete_uncompressed_file()
