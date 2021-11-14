import os

def run(osdir, curpath, args):
    for path in os.listdir(curpath):
        print(str(path))
