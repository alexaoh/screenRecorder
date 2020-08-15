"""main file that records a Firefox page. Especially/originally made to record Zoom-lectures."""

import sys
import time
import subprocess
import signal
from Colors import Colors
from Webdriver import Webdriver
from utils import find_vacant_filename

if len(sys.argv) !=  2:
    raise Exception("The script takes one command line argument, the url to record from.")

url = sys.argv[1] # Get url from terminal argument.

open_webpage = Webdriver(url).get_url().set_fullscreen()

filename = find_vacant_filename()

# After opening the correct url, the recording can begin.
cmd = "ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i :0.0 -f pulse -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor -preset ultrafast -crf 18 -pix_fmt yuv420p "+filename+".mkv"
process = subprocess.Popen(cmd.split(" "))

# Still need to figure out how to change to headphones as output to avoid having output through the speakers when recording. 
# This way I can listen to the lecture / webpage through headphones while recording also! 

# Finish the recording (press ctrl + c in terminal, Python via os package to terminal commands).
time.sleep(15*60) # Sleeps for 91 minutes. 

process.send_signal(signal.SIGINT)
driver.close() # Close the firefox-window when finished recording. 

# Now need to figure out if the machine can be woken up from sleep via BIOS (or something else)
# And use crontab to run the Python-script with the correct url!
# Maybe make another script to change the crontab listing (to change the url) ? Or find a better way to change the url, 
# since this needs to be changed week by week. 

print(Colors.GREEN + "Recording complete!" + Colors.ENDC)

# Compression with ffmpeg
comp_cmd = "ffmpeg -i " + filename + ".mkv -vcodec libx265 -preset ultrafast " + filename + ".mp4"
compression = subprocess.Popen(comp_cmd.split(" "))
returncode = compression.wait()
print(Colors.CYAN + "Returncode: " + str(returncode) + Colors.ENDC)
compression.send_signal(signal.SIGINT)

print(Colors.GREEN + "Compression complete!" + Colors.ENDC)
