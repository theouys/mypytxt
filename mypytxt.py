import writeoutfile
import help
import append
import count
import insert
import copyfile
import display
import os.path
import replaceall
import pathlib
from os import path

print("====================================")
print("mypytxt - Your text file manupilator.")
print("====================================")
inptcommand = ""
sourcefile = ""
outfile = ""
sourcefile = input("Enter source file's full path. ")
if (path.exists(sourcefile)):
     outfile = sourcefile+".out"
else:
    input("Not a valid file. Goodbye!")  
    inptcommand = "exit"  

commandfound=0
while (inptcommand != "exit"):
       

    if (path.exists(sourcefile)):
        outfile = sourcefile+".out"
        inptcommand = input("~] ")
    else:
        input("Not a source file. Goodbye!")  
        inptcommand = "source"  

    

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
    # Display Help
    #-------------------------------------------------------
    if(inptcommand == "help"):
      commandfound=1 
      help.printhelp()

    #-------------------------------------------------------
    # Count lines
    #-------------------------------------------------------
    if(inptcommand == "count"):
      commandfound=1 
      yesno = input("Count lines in source or destination ? (s/d) ")
      if(yesno=="s"):
        print("Count lines in source "+sourcefile)
        count.Count(sourcefile)      
      else:  
        print("Count lines in destination "+outfile)
        count.Count(outfile)    
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
    if(inptcommand == "replace"):
      commandfound=1 
      fromtxt = input("Enter string to replace. ")
      totxt = input("Enter string to use. ")
      replaceall.Replace(sourcefile,outfile,fromtxt,totxt)    

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
    # Copy source
    #-------------------------------------------------------
    if(inptcommand == "copy"):
      commandfound=1 
      copyfile.Copy(sourcefile,outfile)      

    #-------------------------------------------------------
    # Concat source
    #-------------------------------------------------------
    if(inptcommand == "concat"):
      commandfound=1 
      copyfile.Concatenate(sourcefile,outfile)        

    #-------------------------------------------------------
    # Concat x number of times source
    #-------------------------------------------------------
    if(inptcommand == "concatx"):
      commandfound=1 
      xtimes = input("Enter x number of times to concat. ")
      copyfile.Concat_ntimes(sourcefile,outfile, int(xtimes))      

    #-------------------------------------------------------
    # Rename source
    #-------------------------------------------------------
    if(inptcommand == "rename"):
      commandfound=1 
      newfile = input("Enter new name for "+ sourcefile+" ")
      os.rename(sourcefile,newfile)
      sourcefile = newfile

    #-------------------------------------------------------
    # Rename source
    #-------------------------------------------------------
    if(inptcommand == "remove"):
      commandfound=1 
      yesno = input("Remove source or destination ? (s/d) ")
      if(yesno=="s"):
        if (path.exists(sourcefile)):
         os.remove(sourcefile)
      else:  
        if (path.exists(outfile)):
         os.remove(outfile)

      
 

    #-------------------------------------------------------
    # Display output file file
    #-------------------------------------------------------
    if(inptcommand == "display"):
      commandfound=1 
      yesno = input("Display source or destination ? (s/d) ")
      if(yesno=="s"):
        print("Displaying source "+sourcefile)
        display.Display(sourcefile)      
      else:  
        print("Displaying destination "+outfile)
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