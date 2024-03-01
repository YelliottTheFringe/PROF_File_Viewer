import sys as s
from time import sleep
import eSYS as e
import random as r
# To-do: add cutom print function
add_sudo=["add","Add"]
remove_sudp=["Rem","Remove","remove","rem"]
mod_sudo=["mod","Mod"]
y_sudo=["y","Yes","Y","Ye","yes","ye"]
n_sudo=["N","n","No","no"]
filepathtype=input("File is new? y/n ")

while True:
    if filepathtype in y_sudo:
        selected_file=input("File path: ")
        break
    elif filepathtype in n_sudo:
        try:
            filename=input("Filename? Exclude the extension. ")
            filename= filename+".prof"
            selected_file=filename
            with open (filename,"x") as f:
                f.close()
                break
            
        except:
            print("File already exsists: {",selected_file,"}")

# Opperation type. To-do: removal locator and data modifier based on header.
Operation = input("Opperation? (Add, Remove, Modify)")
opperation_Complete = False
while opperation_Complete is False:
    #write to the file, appending
    if Operation in add_sudo:
        opp_header = input("Header data: ")
        opp_inf = input("Information: ")
        with open(selected_file,"a") as profile:
            full_text=opp_header+"-"+opp_inf
            full_text=e.encode_to_STR(full_text,r.randint(1,20))
            #find the character length of the message and add an indicator
            char_count=0
            for i in full_text: # gives me a character count of the full encyrpted message. Useful for decryption!
                char_count+=1
            if char_count<100:
                full_text=("0"+str(char_count)+"c")+full_text 
            else:
                full_text=(str(char_count)+"c")+full_text
            profile.write(full_text+"\n")
            profile.close()
    #write to the file, unencoded append
    if Operation == "a -nec":
        opp_header = input("Header data: ")
        opp_inf = input("Information: ")
        full_text=opp_header+"-"+opp_inf+"\n"
        with open(selected_file,"a") as profile:
            profile.writelines(full_text)
            profile.close()
    #view, encrypted
    if Operation == "view" or Operation == "view":
        with open(selected_file,"r") as f:
            print(f.read())
    #view, decrypted
    if Operation =="view -d":
        with open(selected_file,"r") as f:
            fileTotal=f.read(-1)
            fileTotalList=[]
            currentLine=""
            fileTotal_unencrypted=""
            # parse entire file into a list of characters
            if not fileTotal=="":
                for i in fileTotal: 
                    fileTotalList.append(i)
                fileTotalList.remove("\n")
                char_count=0
                # check for indicators and steal the indicated number of characters into the current message
                for i in range(0,len(fileTotalList)): #parse by line
                    if fileTotalList[i]=='c':
                            char_count=fileTotalList[i-3]+fileTotalList[i-2]+fileTotalList[i-1]
                            char_count=int(char_count)
                            for c in range(1,char_count+1):
                                currentLine+=fileTotalList[i+c]

                            fileTotal_unencrypted+=(e.STRdecode_to_STR(currentLine)+"\n")
                    currentLine=""
                print(fileTotal_unencrypted)
            else:
                print("File is empty.")
            f.close()
    #erase current contents
    if Operation =="clear":
        with open(selected_file,"w") as f:
            f.write("")
            f.close()
    elif Operation =="quit":
           break
           
    Operation = input("Opperation? ")
