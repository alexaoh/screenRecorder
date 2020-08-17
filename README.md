## Screen Recorder made on Ubuntu 20.04 LTS, but I imagine it works on mac also (uses subprocess module for Python for Bash commands) 

### Requirements
* Python
* Selenium (for Python)
* Webdriver for Firefox (Geckodriver)
* FFmpeg
* Zoom Redirector Firefox extension to stop Zoom from opening in the desktop app. 

I recommend making a virtual environment from 'dependencies.yml'. 

This was made originally to record Zoom-lectures automatically, since my lecturer did not want to record them and attending them was not possible for me. Remember to ask for permission before recording anyone :)

Use crontab to schedule your recordings. 

### Usage

Run the script like the following:

> python main.py [url to record from]

The script assumes that the url is a Zoom-meeting if it contains the string 'zoom' in the url. 
In this case it uses the installed extension Zoom Redirector to open the meeting in the browser and do the following steps to take you to the meeting. 
