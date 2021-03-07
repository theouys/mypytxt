def Display(sourcefile):
    filepath = sourcefile
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print(line.strip("\n"))
            if (cnt > 20) :
                break
            line = fp.readline()
            cnt += 1

          