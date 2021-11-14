import os

def run(osdir, username, curpath, args):
    for path in os.listdir(curpath):
        print(str(path))
