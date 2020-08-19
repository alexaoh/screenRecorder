"""File for recording the screen with FFmpeg."""

import sys
# The path to the partent directory is added to be able to import from it below.
path = sys.path[0].split("/")
sys.path.append("/".join(path[:-1])+"/")

from utils import find_vacant_filename
from FFmpeg_util import FFmpeg_util

filename = find_vacant_filename()

recorder = FFmpeg_util("/".join(path)+"/"+filename)

# Record for 95 minutes to be sure that the entire lecture is recorded. 
recorded = recorder.record_screen_with_audio(minutes = 0.5) 

recorded.compress_file().delete_uncompressed_file()
