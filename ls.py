import os

def run(curpath, args):
    for path in os.listdir(curpath):
        print(str(path))
