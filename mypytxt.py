import writeoutfile
import help
import append
import insert
import copyfile
import display
import os.path
import replaceall
import pathlib
from os import path

print("====================================")
print("mytxt - Your text file manupilator.")
print("====================================")
inptcommand = ""
sourcefile = ""
outfile = ""
#sourcefile = input("Enter source file's full path. ")
#outfile = input("Enter destination file's full path. ")
#if (path.exists(sourcefile)):
#    print("")
#else:
#    input("Not a valid file. Goodbye!")  
#    inptcommand = "exit"  

commandfound=0
while (inptcommand != "exit"):
    inptcommand = input("~] ")
    sfile = pathlib.Path(sourcefile)
    ofile = pathlib.Path(outfile)

    if  sfile.exists(): x=0
    else: sourcefile = input("Enter source file's full path.. ")

    if ofile.exists(): x=0
    else: 
        outfile = input("Enter destination file's full path.. ")
        writeoutfile.write(outfile,"")

    if (sourcefile == outfile):
        print("Source and destination cannot be the same")
        sourcefile = input("Enter source file's full path. ")
        outfile = input("Enter destination file's full path. ")

    


    #-------------------------------------------------------
    # Display Source and Destination files
    #-------------------------------------------------------
    if(inptcommand == "?"):
      commandfound=1 
      print("Source: " + sourcefile)
      print("Destination: " + outfile)
      print("")
      print("If you are looking for help, type help and enter.")

    #-------------------------------------------------------
    # Specify a new Source File
    #-------------------------------------------------------
    if(inptcommand == "source"):
      commandfound=1 
      sourcefile = input("Enter source file's full path. ")

    #-------------------------------------------------------
    # Specify a new desitnation File
    #-------------------------------------------------------
    if(inptcommand == "destination"):
      commandfound=1 
      outfile = input("Enter destination file's full path. ")

    #-------------------------------------------------------
    # Display Help
    #-------------------------------------------------------
    if(inptcommand == "help"):
      commandfound=1 
      help.printhelp()

    #-------------------------------------------------------
    # Append string to file
    #-------------------------------------------------------
    if(inptcommand == "replaceall"):
      commandfound=1 
      fromtxt = input("Enter string to replace. ")
      totxt = input("Enter string to use. ")
      replaceall.ReplaceAll(sourcefile,outfile,fromtxt,totxt)  

    #-------------------------------------------------------
    # Append string to file
    #-------------------------------------------------------
    if(inptcommand == "append"):
      commandfound=1 
      stringtoappend = input("Enter string to append. ")
      append.AppendToFile(sourcefile,outfile,stringtoappend)  

    #-------------------------------------------------------
    # swop make destination the new source
    #-------------------------------------------------------
    if(inptcommand == "swop"):
      commandfound=1 
      copyfile.Copy(outfile,sourcefile)    


    #-------------------------------------------------------
    # Clone source
    #-------------------------------------------------------
    if(inptcommand == "copy"):
      commandfound=1 
      copyfile.Copy(sourcefile,outfile)      

    #-------------------------------------------------------
    # Display output file file
    #-------------------------------------------------------
    if(inptcommand == "display"):
      commandfound=1 
      display.Display(outfile)    

    #-------------------------------------------------------
    # Insert string to file
    #-------------------------------------------------------
    if(inptcommand == "insert"):
      commandfound=1 
      stringtoappend = input("Enter string to insert. ")
      insert.InsertToFile(sourcefile,outfile,stringtoappend)    

    #-------------------------------------------------------
    # Run embedded OS shell   
    #-------------------------------------------------------
    if(inptcommand == "!"):
        commandfound=1
        inptoscommand = "" 
        while (inptoscommand != "exit"): 
            try:
                inptoscommand = input("OS> ")
                if(inptoscommand[0:2]=="cd"):
                    if(inptoscommand=="cd"):
                        os.chdir("./~")
                    else : os.chdir(inptoscommand[3:])
                os.system(inptoscommand)      
            except Exception as e:
                print("Oops!", e.__class__,"occurred")
    #-------------------------------------------------------
    
    #Leave these lines at the bottom            
    if(commandfound < 1):
        print("Command not valid")          
    commandfound = 0    
print("Written By: Theo Uys")   