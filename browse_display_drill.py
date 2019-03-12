"""Drill Description

Drill Description:
For this drill, you will need to write a script that creates a GUI
with a button widget and a text widget. Your script will
also include a function that when it is called will invoke a dialog modal
which will allow users with the ability to select a folder directory from their system.
Finally, your script will show the user’s selected directory path into the text field.

"""
#import tkinter
import tkinter as tk
from tkinter import *
#import sqlite and os commands
import os
import sqlite3
import tkinter.filedialog



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')

       
        #needs a button widget
        self.btn_browse = tk.Button(self.master,width=12,height=2,text='Choose Program',command=self.choose_dir)
        self.btn_browse.grid(row=1,column=0,padx=(10,40),pady=(5,0), sticky=E)
        #needs a text widget
        self.lblDisplay = Label(self.master, text='Your chosen directory will go here', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=0, column=0, padx=(30,0), pady=(30,0), sticky=W+E)
        
    def choose_dir(self):
        dir_name = tk.filedialog.askdirectory()
        self.lblDisplay.config(text='{}'.format(dir_name))
        
        



        """function that when it is called will invoke a dialog modal
        which will allow users with the ability to select a folder directory from their system.
        Finally, your script will show the user’s selected directory path into the text field."""
        #Your script will need to use the askdirectory() method from the Tkinter module.
        """
        Your script will need have a function linked to the button widget so that
        once the button has been clicked
        will take the user’s selected file path retained by the askdirectory() method
        and print it within your GUI’s text widget.
        """


        
        
        

    
        




















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
