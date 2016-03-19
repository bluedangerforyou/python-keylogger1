# python-keylogger1
#Python keylogger that emails log to gmail account.
#Version 1.
#This python code creates a file in AppData/Roaming containing the keystrokes.
#At each run, the log will be emailed to supplied gmail account. You must supply it in the .pyw file.
#This is beta version and is Ran on Windows OS.
#THINGS TO DO:
#Add code to run keylogger in startup items for persistence.  
#Add code to hide from task manager.
#Add loop for email at time interval - currently sends once per execution, but goal is to set it to send every 3 hours.
#Clear previous data from log to save space and avoid repeating data.
#Add screen shots when a new window is opened.
#

#NOTE: This can be compiled into exe using PyInstaller or Py2exe and option set to no console for stealth
#IMPORTANT- you MUST supply email address and password in file first or keylogger will not work!
