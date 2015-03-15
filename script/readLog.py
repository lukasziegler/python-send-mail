import csv
import re
import sendMail

### Configuration

# path to logfiles
logPath = 'C:/Users/pervasive/Dropbox/Lukas Ziegler/logs/'
# name of logfile to evaluate
logFile = 'logFile.txt'
# column to evaluate
column = 2	# start counting by 0 by evaluating

	### LogFile Overview ###
	## 1. ID		# 4. Choice
	## 2. Date		# 5. FinalStage
	## 3. Email  >> column = 2


### Helper functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


lastLine = -1

### Check where the Scheduler last left off
lineLog = open(logPath + 'lastLine.txt', 'r')
lastLine = lineLog.read()
print "lastLine:",lastLine


### READ SURVEY LOG (line by line)
i = 0
surveyLog = open(logPath + logFile)
for line in csv.reader(surveyLog, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.

	## Check if Email is Valid
	if i >= int(lastLine) and re.match(r"[^@]+@[^@]+\.[^@]+", line[3]):
		# print "Send email to:",line[column]
		# print "new line",i
		sendMail.send(line[column])

	i += 1

surveyLog.close()


### UPDATE LAST LINE-LOG
if int(lastLine) != i:	# only update if new line was processed
	lastLine = i
	print "new lastLine:",lastLine

	lineLog = open(logPath + 'lastLine.txt', "wb")
	lineLog.write(str(lastLine))
	lineLog.close()
