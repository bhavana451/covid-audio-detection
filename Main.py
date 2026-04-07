import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pre
import recordingaudio as ras
import CNNLSTM as tr
import Predict as pm
import training as itr
import prediction as ipr
import testsms as sms


bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
        global window
        def clear():
            print("Clear1")
            txt.delete(0, 'end')    
            txt1.delete(0, 'end')
            txt2.delete(0, 'end')
            txt3.delete(0, 'end')
            txt4.delete(0, 'end')
  



        window = tk.Tk()
        window.title("Covid-19 Prediction Using Coughing Pattern")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Covid-19 Prediction Using Coughing Pattern" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=20)

        lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=120)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=135)

        lbl1 = tk.Label(window, text="Select Dataset(CSV)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=100, y=190)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=400, y=205)

        lbl3 = tk.Label(window, text="Enter file name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=100, y=260)
        
        txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=400, y=275)
        lbl2 = tk.Label(window, text="Select Audio File",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=330)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=400, y=345)
        lbl4 = tk.Label(window, text="Select X-ray Image",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=100, y=400)
        
        txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt4.place(x=400, y=415)
        
        lbl5 = tk.Label(window, text="Enter Patient Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl5.place(x=100, y=470)
        
        txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt5.place(x=400, y=485)
        lbl6 = tk.Label(window, text="Patient Mobile Number",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl6.place(x=100, y=540)
        
        txt6 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt6.place(x=400, y=555)


        def browse():
                path=filedialog.askdirectory()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select DataSet Folder")     

        def browse1():
                path=filedialog.askopenfilename()
                print(path)
                txt1.delete(0, 'end')
                txt1.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Datset")     

        def browse2():
                path=filedialog.askopenfilename()
                print(path)
                txt2.delete(0, 'end')
                txt2.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Audio File")
        def browse3():
                path=filedialog.askopenfilename()
                print(path)
                txt4.delete(0, 'end')
                txt4.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Image File")
        def recaudio():
                fname=txt3.get()
                if fname !="":
                        ras.process(fname)
                        tm.showinfo("Success", "Audio file stored in D drive")
                else:
                        tm.showinfo("Input error", "Enter audio file name")
                        
                        
                        

        def preproc():
                sym=txt.get()
                if sym != "" :
                        pre.process(sym)
                        print("preprocess")
                        tm.showinfo("Output", "Preprocess Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset")
        def Training():
                sym=txt.get()
                if sym != "" :
                        print("CNN-LSTM Training")
                        tr.process(sym)
                        tm.showinfo("Output", "Training Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset")
        
        def Predictprocess():
                sym=txt2.get()
                sym1=txt4.get()
                sym2=txt5.get()
                sym3=txt6.get()
                if sym != "" and sym1!="" and sym2 != "" and sym3!="":
                        result=pm.process(sym)
                        tm.showinfo("Output", "Prediction of audio : " +str(result))
                        iresult=""
                        res=ipr.process(sym1)
                        if res==0:
                                iresult="Covid Affected"
                        if res==1:
                                iresult="No-Covid"
                        tm.showinfo("Output", "Prediction of image :   "+str(iresult))
                        finalpred=""
                        if result=="Covid+ve" and iresult=="Covid Affected":
                                finalpred="Severly covid attacked"
                        if result=="Non-Covid" and iresult=="Covid Affected":
                                finalpred="Intermediate covid attacked"
                        if result=="Covid+ve" and iresult=="No-Covid":
                                finalpred="Intermediate covid attacked"
                        if result=="Non-Covid" and iresult=="No-Covid":
                                finalpred="No Covid"
                        tm.showinfo("Output", "Final Prediction :   "+str(finalpred))
                        msg="Dear "+sym2+", \nYour COVID Test Result is "+str(finalpred)
                        mob=sym3
                        sms.process(msg,mob)
                        
                                
                                
                else:
                        tm.showinfo("Input error", "Select Audio and image File enter patient name and mobile number")
                        

        browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=650, y=135)

        browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse1.place(x=650, y=205)

        browse2 = tk.Button(window, text="Browse", command=browse2  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse2.place(x=650, y=345)
        browse3 = tk.Button(window, text="Browse", command=browse3  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse3.place(x=650, y=415)

        rec = tk.Button(window, text="Record Audio", command=recaudio  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        rec.place(x=650, y=275)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=950, y=200)
         
        proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        proc.place(x=100, y=600)
        

        SVMbutton = tk.Button(window, text="Training", command=Training  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVMbutton.place(x=300, y=600)
        

        PRbutton = tk.Button(window, text="Predict", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        PRbutton.place(x=500, y=600)

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=700, y=600)

        window.mainloop()
Home()

