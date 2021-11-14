import os

def run(setpathfunc, osdir, username, curpath, args):
    for path in os.listdir(curpath):
        if os.path.isfile(path):
            print("[FILE] " + str(path))
        elif os.path.isdir(path):
            print("[DIR] " + str(path))
