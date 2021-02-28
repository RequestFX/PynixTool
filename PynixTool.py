import os
import math

def printLogo():
    print(
            "██████╗ ██╗   ██╗███╗   ██╗██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗"
        + "\n██╔══██╗╚██╗ ██╔╝████╗  ██║██║╚██╗██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║"
        + "\n██████╔╝ ╚████╔╝ ██╔██╗ ██║██║ ╚███╔╝    ██║   ██║   ██║██║   ██║██║"
        + "\n██╔═══╝   ╚██╔╝  ██║╚██╗██║██║ ██╔██╗    ██║   ██║   ██║██║   ██║██║"
        + "\n██║        ██║   ██║ ╚████║██║██╔╝ ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗"
        + "\n╚═╝        ╚═╝   ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n")

    print("> PynixTool v1.0 made by RequestFX#1541 <\n")

def fileSize_(fileSize):

    size = [[0 for x in range(2)] for y in range(2)]

    if(fileSize > 1024 * 10 ** 3):
        size[0][0] = round(fileSize / (1024 * 10 ** 3), 2)
        size[0][1] = "MB"
    else:
        size[0][0] = math.ceil(fileSize / 1024)
        size[0][1] = "KB"

    return size

def scriptList(dir):

    scripts = []
    i = 0

    for file in os.listdir(dir):
        d = os.path.join(dir, file)
        if(d.lower() != __file__.lower() and d.endswith(".py")):
            scripts.append(d)
            fileSize = fileSize_(os.path.getsize(d))
            print("["+str(i)+"] > " + os.path.basename(d) + " | " + str(fileSize[0][0]) + " " + str(fileSize[0][1]))
            i = i + 1

    return scripts

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

printLogo()
scripts = scriptList(os.getcwd())

while True:
    if(len(scripts) == 0):
        print("Error! No Scripts Found in Current Path > " + os.getcwd())
        dir = input("Please Enter a Directory > ")
        print("")
        scripts = scriptList(dir)
    else:
        break

print("")
script = 0

while True:
    script = input("Please Enter a Number between 0 - " + str(len(scripts) - 1) + " To open your choosen .py Script: ")
    if(isInt(script) and int(script) >= 0 and int(script) < len(scripts)):
        break

print("Trying to Start Script...\n-------------------------------------------------------------------------\n")
os.system(scripts[int(script)])
