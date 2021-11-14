import os

def run(setpathfunc, osdir, username, curpath, args):
    for path in os.listdir(curpath):
        print(str(path))
