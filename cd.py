import os

def run(setpathfunc, osdir, username, curpath, args):
    if len(args) != 2:
        print("Usage:")
        print("\tcd [dir]")
    else:
        if os.path.exists(curpath + "/" + args[1]):
            setpathfunc(os.path.normpath(curpath + "/" + args[1]))
