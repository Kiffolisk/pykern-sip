import os

def run(setpathfunc, osdir, username, curpath, args):
    for path in os.listdir(curpath):
        # i hate this
        if os.path.isfile(curpath + path) == True:
            print("[FILE] " + str(path))
        if os.path.isdir(curpath + path) == True:
            print("[DIR] " + str(path))
