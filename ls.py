import os

def run(setpathfunc, osdir, username, curpath, args):
    for path in os.listdir(curpath):
        if os.path.isfile(path) == True:
            print("[FILE] " + str(path))
        if os.path.isdir(path) == True:
            print("[DIR] " + str(path))
