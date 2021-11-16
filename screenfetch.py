import os

def run(funcs, ivars):
    if not len(ivars) > 4:
        print("This package is not compatible with your kernel version!")
        return
    setpathfunc = funcs[0]
    args = ivars[3]
    curpath = ivars[2]
    osdir = ivars[0]
    username = ivars[1]
    sfetch = ivars[4]
    for x in range(len(sfetch)):
        print(sfetch[x])
