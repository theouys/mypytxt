import writeoutfile
import os.path
import pathlib
from os import path

def Copy(sourcefile,outfile):
    filepath = sourcefile
    if (path.exists(outfile)):
        os.remove(outfile)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1