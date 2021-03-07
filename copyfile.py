import writeoutfile

def Copy(sourcefile,outfile):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1