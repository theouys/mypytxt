
def write(filename, txt):
  file = open(filename,'a')
  file.write(txt+"\n")
  file.close