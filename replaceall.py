import writeoutfile
import os.path
import pathlib
from os import path

def ReplaceAll(sourcefile,outfile,fromtxt,totxt):
    filepath = sourcefile
    if (path.exists(outfile)):
        os.remove(outfile)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            changeline = changeline.replace(fromtxt,totxt)
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1

def Replace(sourcefile,outfile,fromtxt,totxt):
    filepath = sourcefile
    if (path.exists(outfile)):
        os.remove(outfile)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            print(changeline)
            yesno = input("Do this line (y/n)? ")
            if (yesno=="y"):
              changeline = changeline.replace(fromtxt,totxt)
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1            

          