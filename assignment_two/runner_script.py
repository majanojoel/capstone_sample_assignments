import subprocess, os.path, json
from pathlib import Path


#Colors
T_CLR_MSG = '\033[94m'
T_CLR_WARN = '\033[93m'
T_CLR_ERROR = '\033[91m'
T_CLR_SUCCESS = '\033[92m'
T_CLR_TERMINATOR = '\033[0m'

def printText(type, text):
    print(f"{type}{text}\n{T_CLR_TERMINATOR}")


#### HELPER FUNCTIONS #######

def generateArgs(plugin, args):
    argString = ""
    for arg in args:
        argString+=f" -fplugin-arg-{plugin}-{arg}"
    return argString

printText(T_CLR_MSG, "Welcome to v0.5 of this script!")
data = {}
# Opening JSON file
with open('script-config.json', 'r') as f:
    # returns JSON object as a dictionary
    data = json.load(f)
  
if data == {}:
    printText(T_CLR_ERROR, "Failed to load JSON file. Exiting!")
    quit()

pluginDict = data['clang-plugins']

#generate file list
fileList = []
CPPfileList = list(Path(".").rglob("*.[c][p][p]")) #CPP files
CfileList = list(Path(".").rglob("*.[c]")) #C files

if(len(CPPfileList) == 0):
    fileList = list(CfileList)
else:
    fileList = list(CPPfileList)

#### LINKS ####

printText(T_CLR_MSG, "Downloading required plugins. Please wait.")
for plugin in pluginDict:
    if os.path.isfile(f"{plugin}.so"): continue
    output=subprocess.getoutput(f"curl -L0 https://github.com/majanojoel/ECE496_ClangPlugins/raw/main/libraries/{plugin}_stable.so -o {plugin}.so")
    # Check if plugin downloaded
    if not os.path.isfile(f"{plugin}.so"):
        printText(T_CLR_ERROR, f"Couldn't download {plugin}.so. Exiting!")
        quit()

printText(T_CLR_SUCCESS, "Plugins downloaded. Running checks next.")

testsPassed = True
######## Checks ##############
for file in fileList:
    for plugin, pluginArg in pluginDict.items():
        printText(T_CLR_MSG, f"Running {plugin} check on {str(file)}")
        argString = ''
        if pluginArg != '' and plugin != "recursive_functions":
            argString = generateArgs(plugin, pluginArg)
        output=subprocess.getoutput(f"clang-15 -fplugin=./{plugin}.so{argString} -c {str(file)}")
        if(output != ""): 
            testsPassed = False
            printText(T_CLR_ERROR, output)
        else:
            printText(T_CLR_SUCCESS, f"{plugin} check passed!")

######## Compilation #########
if(testsPassed):
    printText(T_CLR_SUCCESS, "All checks passed, running make next!")
    output = subprocess.getoutput("make")
    printText(T_CLR_MSG, "Make Output:")
    print(output + "\n")
    printText(T_CLR_SUCCESS, "Script complete! Please test your program or if make failed, fix the problems and run again.")
else: 
    printText(T_CLR_WARN, "One or more tests failed. Please fix the errors in your code and retry running the script.")
