import subprocess
import signal
import time
from Colors import Colors

class FFmpeg_util:
    """Class that uses subprocess to envoke FFmpeg commands in terminal. 

    Has methods for recording screen, compressing the recorded file afterwards and deleting the non-compressed file. 
    """
    
    def __init__(self, filename):
        self.filename = filename

    def record_screen_with_audio(self, minutes):
        """Record monitor video and audio. Save as .mk4 (uncompressed) in . directory."""
        #cmd = "/usr/bin/ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i :0.0 -f pulse -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor -preset ultrafast -crf 18 -pix_fmt yuv420p "+self.filename+".mkv"
        #cmd = "ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i :0.0 -f pulse -i "+ "/etc/pulse/default.pa" +" -preset ultrafast -crf 18 -pix_fmt yuv420p "+self.filename+".mkv"
        # Kommandoen nedenfor ga ingen lyd! Den gir connection refused via crontab uansett!
        cmd = "/usr/bin/ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i :0.0 -f alsa -ac 2 -i pulse -acodec aac -strict experimental -preset ultrafast -crf 18 -pix_fmt yuv420p "+self.filename+".mkv"
        process = subprocess.Popen(cmd.split(" "))

        # Still need to figure out how to change to headphones as output to avoid having output through the speakers when recording. 
        # This way I can listen to the lecture / webpage through headphones while recording also! 

        time.sleep(minutes*60) # Sleeps for 'minutes' minutes. 

        # Finish the recording (press ctrl + c in terminal)
        process.send_signal(signal.SIGINT)

        # Now need to figure out if the machine can be woken up from sleep via BIOS (or something else)
        # And use crontab to run the Python-script with the correct url!
        # Maybe make another script to change the crontab listing (to change the url) ? Or find a better way to change the url, 
        # since this needs to be changed week by week. 

        print(Colors.GREEN + "Recording complete!" + Colors.ENDC)
        return self

    def compress_file(self):
        """Compress recorded file in . directory and make new .mp4 with the same name."""
        comp_cmd = "ffmpeg -i " + self.filename + ".mkv -vcodec libx265 -preset ultrafast " + self.filename + ".mp4"
        compression = subprocess.Popen(comp_cmd.split(" "))
        returncode = compression.wait()
        print(Colors.CYAN + "Returncode: " + str(returncode) + Colors.ENDC)
        compression.send_signal(signal.SIGINT)

        print(Colors.GREEN + "Compression complete!" + Colors.ENDC)
        return self

    def delete_uncompressed_file(self):
        """Delete uncompressed file from . directory."""
        cmd = "rm -f " + self.filename +".mkv"
        subprocess.Popen(cmd.split(" "))

        print(Colors.GREEN + "Uncompressed file was successfully deleted!" + Colors.ENDC)
