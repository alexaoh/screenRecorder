## Screen Recorder made on Ubuntu 20.04 LTS, but I imagine it works on mac also (uses subprocess module for Python for Bash commands) 

### Requirements
* Python
* Selenium (for Python)
* Webdriver for Firefox (Geckodriver)
* FFmpeg
* 'Zoom Redirector' extension to stop Zoom from opening in the desktop app. 
* 'Buster: Captcha Solver for Humans' extension.

I recommend making a virtual environment from 'dependencies.yml'. 

This was made originally to record Zoom-lectures automatically, since my lecturer did not want to record them and attending them was not possible for me. Remember to ask for permission before recording anyone :)


### Usage

Run the script like the following:

> python main.py [url to record from]

The script assumes that the url is a Zoom-meeting if it contains the string 'zoom' in the url. 
In this case it uses the installed extension Zoom Redirector to open the meeting in the browser and do the following steps to take you to the meeting. 

You can also run the script manually via 'job.sh', by following the two bulletpoints below. 

### Set up job via cron

* Add a file name 'URL.sh' which conatins the following 
> URL="\<The url you want to open\>"

* Make script executable. Run the following command in the terminal. 
> chmod +x job.sh

* Add a new job to crontab. This is done by editing the file that opens with the command 
> crontab -e  

The job should have the specified format. 
E.g: 

> 44 15 * * 3 export DISPLAY=:0 && /\<absolute path to file\>/job.sh > /\<absolute path to file\>/cron.log 2>&1

The command given above runs 'job.sh' on the display at 15:44 every Wednesday. 

This is by no means a finished project and could be vastly improved. However, I can use it as originally planned. We shall see if I find the time to improve it. Feel free to contribute with a PR if you find this interesting :)
