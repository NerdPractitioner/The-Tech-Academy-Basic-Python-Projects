
#import tkinter
import tkinter as tk
from tkinter import *
#import sqlite and os commands
import os
import sqlite3
import tkinter.filedialog
import shutil



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(1000, 200))
        self.master.title('Move Text Files')
        #variables
        self.varSrc = StringVar()
        self.varDest = StringVar()
        self.varTxtFiles = []

        
        #display labels
        self.lblSrc = Label(self.master, text='Source: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblSrc.grid(row=2, column=0,padx=(30,0), pady=(30,0), sticky=W)

        self.lblDest = Label(self.master, text='Destination: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDest.grid(row=2, column=3,padx=(30,0), pady=(30,0), sticky=W)

        
        #text displays
        self.displaySrc = Label(self.master, text='Your Source directory will go here', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.displaySrc.grid(row=0, column=0, rowspan=2, columnspan=2, padx=(30,0), pady=(30,0), sticky=W+E)
        
        self.displayDest = Label(self.master, text='Your Destination directory will go here', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.displayDest.grid(row=0, column=3, rowspan=2, columnspan=2, padx=(30,0), pady=(30,0), sticky=W+E)

    
        #buttons
        self.btnBrowseSrc = tk.Button(self.master,width=12,height=2,text='Set Source',command=self.set_src)
        self.btnBrowseSrc.grid(row=3,column=1,padx=(10,40),pady=(5,0), sticky=E)

        self.btnBrowseDest = tk.Button(self.master,width=12,height=2,text='Set Destination',command=self.set_dest)
        self.btnBrowseDest.grid(row=3,column=3,padx=(10,40),pady=(5,0), sticky=W)
        
        self.btnMove = tk.Button(self.master,width=12,height=2,text='Move',command=self.txt_move)
        self.btnMove.grid(row=3,column=2,padx=(10,40),pady=(5,0), sticky=E)

        self.create_db()
        
        

    #functions  plan to use varSrc and varDest to tell txt_move which paths to use
    def create_db(self):
        conn = sqlite3.connect('db_file_train.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_file_train( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_path TEXT, \
                col_mtime TEXT \
                );")
            conn.commit()
        conn.close()
        
    
    def this_dir(self, dir_name,cur):
        fPath = dir_name
        fList = os.listdir(path=fPath)
        for i in fList:
            var_path = os.path.join(fPath,i)
            if i.lower().endswith(('.txt')):
                var_mtime = os.path.getmtime(i)
                self.varTxtFiles.append(i)
                cur.execute("""INSERT INTO tbl_file_train (col_path,col_mtime) VALUES (?,?)""",(var_path,var_mtime))
        return self.varTxtFiles
        

    def set_src(self):
        conn = sqlite3.connect('db_file_train.db')
        with conn:
            cur = conn.cursor()
            dir_name = tk.filedialog.askdirectory()
            self.lblSrc.config(text='{}'.format(dir_name))
            self.varSrc = dir_name
            self.this_dir(dir_name, cur)
            conn.commit()
        conn.close()            
        return self.varSrc
        
    def set_dest(self):
        dir_name = tk.filedialog.askdirectory()
        self.lblDest.config(text='{}'.format(dir_name))
        self.varDest = dir_name
        return self.varDest

    def txt_move(self):
        conn = sqlite3.connect('db_file_train.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_file_train")
            varFile = cur.fetchall()
            for item in varFile:
                msg = "File Path: {}\nModified Time: {}".format(item[1],item[2])
                print(msg)
                shutil.move(item[1], self.varDest)

            conn.commit
        conn.close()
        #Your script will need to use the move() method from the Shutil module to cut all qualifying files and paste them within the destination directory.
        

"""

Your script will need to use Python 3, the Tkinter module, and the OS module.

Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.

Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.

Your script will need to use the getmtime() method from the OS module to find out the latest date the file has been created or last modified.

Your script will need to create a database to record the qualifying file and corresponding modified time-stamp.

Your script will need print each file ending with a “.txt” file extension and its corresponding mtime to the console.

Your script will need to use the move() method from the Shutil module to cut all qualifying files and paste them within the destination directory.


"""















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
