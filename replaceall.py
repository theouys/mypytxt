import writeoutfile

def ReplaceAll(sourcefile,outfile,fromtxt,totxt):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            changeline = changeline.replace(fromtxt,totxt)
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1

          