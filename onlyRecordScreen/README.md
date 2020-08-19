## This is made to only record the screen, without opening a browser window. 

Zoom is giving me a hard time, and I do not have time to fix it completely before the first lecture has to be recorded. 
I am therefore opening the meeting in a browser myself. The recording is started with the script and a cronjob. 
Remember to make the script 'record.sh' executable. 
The cron command I used is

> 14 08 * * 4 /\<absolute path to screenRecorder directory\>/screeenRecorder/onlyRecordScreen/record.sh > /\<absolute path to screenRecorder directory\>/screeenRecorder/onlyRecordScreen/cron.log 2>&1

This runs the recording of the screen at 08:14 every Thursday. The part after \> logs the output from the job to the file 'cron.log' in the same directory. 
