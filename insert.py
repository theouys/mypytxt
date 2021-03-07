import writeoutfile

def InsertToFile(sourcefile,outfile,stringtoappend):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            changeline = stringtoappend+ line.rstrip("\n")
            writeoutfile.write(outfile,changeline)
            line = fp.readline()
            cnt += 1

          