import subprocess, time
from pathlib import Path

TIMEOUT_VALUE = 360; #Timeout value in seconds

#find a python file with "tester" in its name

fileList = list(Path(".").rglob("*tester.[p][y]")) #CPP files
if(len(fileList) > 1 or len(fileList) == 0):
    print("Only one tester file must be present in directory structure!")
    exit(1)

testerFilePath = str(fileList[0].resolve())
#start a timer right before running tester
#run script
args = ['python3', testerFilePath]
try:
    startTime = time.time()
    completedProcess = subprocess.run(args, capture_output=True, timeout=TIMEOUT_VALUE)
    endTime = time.time()
except subprocess.TimeoutExpired:
    #handle tester taking too long
    print("Running tester took too long!")


print("Runtime: " + str(endTime-startTime))

#run valgrind