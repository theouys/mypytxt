import writeoutfile
import os.path
import pathlib
from os import path

def Count(sourcefile):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            line = fp.readline()
            cnt += 1
    print("Number of lines="+str(cnt))        