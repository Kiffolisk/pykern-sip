import os

def run(funcs, ivars):
    args = ivars[3]
    curpath = ivars[2]
    if len(args) != 2:
        print("Usage:")
        print("\tcd [dir]")
    else:
        if os.path.exists(curpath + "/" + args[1]):
            setpathfunc(os.path.normpath(curpath + "/" + args[1]))
