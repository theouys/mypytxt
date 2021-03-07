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
def Concatenate(sourcefile,outfile):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1            
def Concat_ntimes(sourcefile,outfile,ntime):
    for i in range(ntime):
        filepath = sourcefile
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                changeline = line.rstrip("\n")
                writeoutfile.write(outfile,changeline)
                line = fp.readline()
                cnt += 1                        