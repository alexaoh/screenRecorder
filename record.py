# Del opp koden i mer logiske deler senere! F.eks én Record-klasse og én klasse som tar seg av å åpne browser. 

# This recorder is especially used for Zoom-lectures in a webpage! These are delivered each week and must be supplied by me. 

from selenium import webdriver
import sys
import os
import time
import subprocess
import signal

if len(sys.argv) !=  2:
    raise Exception("The script takes one command line argument, the url to record from.")

url = sys.argv[1] # Get url from terminal argument.

driver = webdriver.Firefox() # Make a firefox driver. 
driver.get(url)

# If any buttons need to be pressed is individual depending on the webpage used!
driver.maximize_window()

i = 1
while True:
    find = "find . -name out"+str(i)+".mkv"
    search = subprocess.Popen(find.split(" "), stdout=subprocess.PIPE)
    out, err = search.communicate()
    if out.decode('ascii') == "":
        filename = "out" + str(i) + ".mkv" 
        break
    i = i + 1


# After opening the correct url, the recording can begin.
cmd = "ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i :0.0 -f pulse -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor -preset ultrafast -crf 18 -pix_fmt yuv420p "+filename
process = subprocess.Popen(cmd.split(" "))

# Still need to figure out how to change to headphones as output to avoid having output through the speakers when recording. 
# This way I can listen to the lecture / webpage through headphones while recording also! 

# Finish the recording (press ctrl + c in terminal, Python via os package to terminal commands).
time.sleep(5) # Sleeps for 91 minutes. 

process.send_signal(signal.SIGINT)
driver.close() # Close the firefox-window when finished recording. 

# Now need to figure out if the machine can be woken up from sleep via BIOS (or something else)
# And use crontab to run the Python-script with the correct url!
# Maybe make another script to change the crontab listing (to change the url) ? Or find a better way to change the url, 
# since this needs to be changed week by week. 


# Can the video-file be compressed somehow ? It takes a lot of storage as it is right now !
#  