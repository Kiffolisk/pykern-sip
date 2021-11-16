import importlib.util
import os

def run(funcs, ivars):
    setpathfunc = funcs[0]
    args = ivars[3]
    curpath = ivars[2]
    osdir = ivars[0]
    username = ivars[1]
    if len(args) != 2:
        print("Usage:\n\tpy [file]")
    else:
        try:
            loll = open(os.path.normpath(curpath + "/" + args[1]), "r")
            exec(loll.read())
            loll.close()
        except Exception as error:
            print(error)
