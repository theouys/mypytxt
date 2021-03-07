import writeoutfile

def AppendToFile(sourcefile,outfile,stringtoappend):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = line.rstrip("\n")+stringtoappend
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1

          