"""
Drill Description:
For this drill, you will need to write a script that creates a database and adds new data into that database.

Requirements:
Your script will need to use Python 3 and the sqlite3 module.

Your database will require 2 fields, an auto-increment primary integer field and a field with the data type of string.

Your script will need to read from the supplied list of file names at the bottom of this page
and determine only the files from the list which ends with a “.txt” file extension.

Next, your script should add those file names from the list ending with “.txt” file extension within your database.

Finally, your script should legibly print the qualifying text files to the console.

Additional Setup Instructions:
The following is the list of file names to use for this drill:

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
"""

import os
import sqlite3

#run method
def start(txtFiles = []):
    #create an array out of the files in the current directory
    fList,fPath = thisDir()
    #retrieve files ending in .txt
    txtFiles = getTxtFiles(fPath, fList, txtFiles)
    return(txtFiles)

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
            txtFiles.append(i)
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
    #run function start() to gather a list of files ending in .txt
    txtFiles = start()
    #open connection with drill2 database 
    conn = sqlite3.connect('drill2.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill_files( \
            file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT \
            )")

        
        #iterate through text files returned by start
        for i in txtFiles:
            #insert each index from txtFiles to file_name column of tbl_drills    
            cur.execute("INSERT INTO tbl_drill_files(file_name) VALUES (?)", [i])
            conn.commit()


        #select items from tbl_drill_files to print message with item names
        cur.execute("SELECT file_name FROM tbl_drill_files")
        varFile = cur.fetchall()
        print(varFile)
        for item in varFile:
            
            msg = "File Name: {}".format(item[0])
            print(msg)

    conn.close()



















        
