"""
Drill Description:
For this drill, you will need to write a script that will check a specific folder on the hard drive,
verify whether those files end with a “.txt” file extension and
if they do, print those qualifying file names and their corresponding modified time-stamps to the console.

Requirements:
Your script will need to use Python 3 and the OS module.

Your script will need to use the listdir() method from the OS module
to iterate through all files within a specific directory.

Your script will need to use the path.join() method from the OS module
to concatenate the file name to its file path, forming an absolute path.

Your script will need to use the getmtime() method from the OS module
to find the latest date that each text file has been created or modified.

Your script will need to print each file ending with a “.txt” file extension
and its corresponding mtime to the console.

Additional Setup Instructions:
You will need to create a new directory on your system and
then create 10 different files within this folder.
The files that you create should be a combination of any file types you would like
just as long as you include at least two that are text documents ending with a “.txt” file extension.

This directory will be the directory that your script will need to iterate through to complete the drill.
"""

import os

#run method
def start(txtFiles = {}):
    #create an array out of the files in the current directory
    fList,fPath = thisDir()
    #retrieve files ending in .txt
    txtFiles = getTxtFiles(fPath, fList, txtFiles)
    print(txtFiles)

#
def thisDir():
    #I used getcwd instead of the absolute path so this could be used away from my hard drive

    fPath = os.getcwd()  #'D:\\Developing\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\Drills\\'
    fList = os.listdir(path=fPath)
    return fList, fPath
    

def getTxtFiles(fPath, fList, txtFiles):
    #iterate through fList and append .txt files to txtFiles
    for i in fList:
        #going to try to join path here
        os.path.join(fPath, i)
        if i.lower().endswith(('.txt')):
            txtFiles.update({i : os.path.getmtime(i)})
    return txtFiles
"""
def getTxtFiles(fList, txtFiles):
    #iterate through fList and append .txt files to txtFiles
    for i in fList:
        if i.lower().endswith(('.txt')):
            txtFiles.append(i)
    return txtFiles
   """     
    

if __name__ == "__main__":
   # abPath = os.path.join(fPath, fName)
    start()
    
