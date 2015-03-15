# python-send-mail
A python script for sending emails via smtplib from Windows machines, based on the Windows task scheduler evaluating log files.

This script was developed and tested with Python 2.7.9 and pip 1.5.6

## Scope

python-send-mail was created by Lukas Ziegler for his Master's thesis in spring 2015. This approach was chosen due to the conditions given by the surrounding frameworks in which a send mail functionality was to be implemented. The specification was to periodically evaluate a log file containing an email address.

Useful when:

* dependent on Windows machine
* when the master program doesn't support any HTTP calls and doesn't support any email functionality (e.g. smtplib)
* one needs to evaluate log files in order to determine which emails need to be sent

## Usage / Installation

* Copy the files inside the script/ folder to your local machine
* Install python and pip: https://www.python.org/downloads/ & https://pip.pypa.io/en/latest/installing.html
* Make sure the the python and pip environmental variables are set correctly (check by calling `python --version` and `pip --version` from the command line)
* Create a Windows task scheduler, either via [GUI](http://stackoverflow.com/a/25732247/1402076) or via [command line](http://stackoverflow.com/questions/2725754/schedule-python-script-windows-7/2725908#2725908)
* Create an action to call python.exe or pythonw.exe with the batch-file as the second parameter: `C:\Python\python.exe C:\User\Username\Desktop\pythonSchedule.bat`
* Use the .bat file to avoid any problems with incorrect environment variables
* If you want to run Python without seeing the Windows console pop up, use pythonw.exe instead of python.exe.


## Customization

Project files:

    pythonSchedule.bat  # Called by Task Scheduler
    readLog.py          # Evaluating the logfile
    sendMail.py         # Script used to send emails
    logs/
      logfile.txt       # The logfile to scan
      lastLine.txt      # Required to keep track where the script left off

Remarks:
* Use absolute paths throughout the entire script.
* Make sure that the environment variables are set correctly on Windows for python.
* Adjust the `logPath`, `logFile` and `column` to validate for a valid email address inside the `readLog.py` script.
* Adjust `user`, `password`, `sender`, `smtpServer` and the text/html email itself in the `sendMail.py` script.


## Links for troubleshooting

* Forcing smtplib/starttls() to use 'LOGIN PLAIN' for authentication. This setting is required inside of the ifi.lmu.de network provided by RBG / LRZ, since CRAM-MD5 was offered by smtp.ifi.lmu.de, even though it was not supported. [stackoverflow](http://stackoverflow.com/questions/6044677/django-mail-smtplib-auth-method-problem/28672076#28672076)
* Creating a scheduled task on Windows via command line:  [stackoverflow](http://stackoverflow.com/questions/2725754/schedule-python-script-windows-7/2725908#2725908)
* [Sending HTML email using Python](http://stackoverflow.com/questions/882712/sending-html-email-using-python)
* [What is the easiest way to trigger a python script on schedule using Windows 7?](http://stackoverflow.com/questions/25730225/what-is-the-easiest-way-to-trigger-a-python-script-on-schedule-using-windows-7)
* [Python script pops up console when run by scheduler](http://stackoverflow.com/questions/8115492/python-script-pops-up-console-when-run-by-scheduler)
* [Creating a BAT file for python script](http://stackoverflow.com/questions/4571244/creating-a-bat-file-for-python-script)
* [Why do seemingly valid Python scripts fail to run when initiated via the Windows Task Scheduler?](http://stackoverflow.com/questions/11140685/why-do-seemingly-valid-python-scripts-fail-to-run-when-initiated-via-the-windows)
