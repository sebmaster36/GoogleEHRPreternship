#!/usr/bin/env python3

#imports
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from patient import Patient
import os

#constants

rec_dir = "./records/"

root = tk.Tk()
root.title("Preternship Mock EMR")
root.geometry("600x500")
nb = ttk.Notebook(root)

# Patient Visit Collection
page2 = ttk.Frame(nb)

height = ttk.Label(page2, text="Height (cm)").grid(column = 0, row = 0, padx = 30, pady = 15)
weight = ttk.Label(page2, text="Weight (kg)").grid(column = 0, row = 1, padx = 30, pady = 15)
temp = ttk.Label(page2, text="Body Temperature (Celsius)").grid(column = 0, row = 2, padx = 30, pady = 15)
sys = ttk.Label(page2, text="Systolic BP").grid(column = 0, row = 3, padx = 30, pady = 15)
dia = ttk.Label(page2, text="Diastolic BP").grid(column = 0, row = 4, padx = 30, pady = 15)
pulse = ttk.Label(page2, text="Pulse (BPM)").grid(column = 0, row = 5, padx = 30, pady = 15)


eheightvalue = IntVar()
eweightvalue = IntVar()
etempvalue = DoubleVar()
esysvalue = IntVar()
ediavalue = IntVar()
epulsevalue = IntVar()

fnVal = StringVar()
lnVal = StringVar()
gVal = StringVar()
aVal = IntVar()
idVal = IntVar()
heightvalue = IntVar()
weightvalue = IntVar()
tempvalue = DoubleVar()
sysvalue = IntVar()
diavalue = IntVar()
pulsevalue = IntVar()

heightentry = ttk.Entry(page2, textvariable=eheightvalue).grid(column = 1, row = 0, padx = 30, pady = 15)
weightentry = ttk.Entry(page2, textvariable=eweightvalue).grid(column = 1, row = 1, padx = 30, pady = 15)
tempentry = ttk.Entry(page2, textvariable=etempvalue).grid(column = 1, row = 2, padx = 30, pady = 15)
sysentry = ttk.Entry(page2, textvariable=esysvalue).grid(column = 1, row = 3, padx = 30, pady = 15)
diaentry = ttk.Entry(page2, textvariable=ediavalue).grid(column = 1, row = 4, padx = 30, pady = 15)
pulseentry = ttk.Entry(page2, textvariable=epulsevalue).grid(column = 1, row = 5, padx = 30, pady = 15)

# second page
page1 = ttk.Frame(nb)



fname = ttk.Label(page1, text="First Name:").grid(column = 0, row = 0, padx = 30)
fnVal = ttk.Label(page1, text="")
fnVal.grid(column = 1, row = 0, padx = 30, pady=5)
lname = ttk.Label(page1, text="Last Name:").grid(column = 0, row = 1, padx = 30, pady=5)
lnVal = ttk.Label(page1, text="")
lnVal.grid(column = 1, row = 1, padx = 30, pady=5)
id = ttk.Label(page1, text="Patient ID:").grid(column = 0, row = 2, padx = 30, pady=5)
idVal = ttk.Label(page1, text="")
idVal.grid(column = 1, row = 2, padx = 30, pady=5)
gender = ttk.Label(page1, text="Age:").grid(column = 0, row = 3, padx = 30, pady=5)
gVal = ttk.Label(page1, text="")
gVal.grid(column = 1, row = 3, padx = 30, pady=5)
age = ttk.Label(page1, text="Sex:").grid(column = 0, row = 4, padx = 30, pady=5)
aVal = ttk.Label(page1, text="")
aVal.grid(column = 1, row = 4, padx = 30)

height = ttk.Label(page1, text="Height (cm):").grid(column = 0, row = 5, padx = 30, pady=5)
heightvalue = ttk.Label(page1, text="")
heightvalue.grid(column = 1, row = 5, padx = 30)
weight = ttk.Label(page1, text="Weight (kg):").grid(column = 0, row = 6, padx = 30, pady=5)
weightvalue = ttk.Label(page1, text="")
weightvalue.grid(column = 1, row = 6, padx = 30)
temp = ttk.Label(page1, text="Body Temp:").grid(column = 0, row = 7, padx = 30, pady=5)
tempvalue = ttk.Label(page1, text="")
tempvalue.grid(column = 1, row = 7, padx = 30)
sys = ttk.Label(page1, text="Systolic BP:").grid(column = 0, row = 8, padx = 30, pady=5)
sysvalue = ttk.Label(page1, text="")
sysvalue.grid(column = 1, row = 8, padx = 30)
dia = ttk.Label(page1, text="Diastolic BP:").grid(column = 0, row = 9, padx = 30, pady=5)
diavalue = ttk.Label(page1, text="")
diavalue.grid(column = 1, row = 9, padx = 30)
pulse = ttk.Label(page1, text="Pulse (bpm):").grid(column = 0, row = 10, padx = 30, pady=5)
pulsevalue = ttk.Label(page1, text="")
pulsevalue.grid(column = 1, row = 10, padx = 30)

def getSum(Patient):
    Patient.summary()

eBtn = ttk.Button(page1, text="Export Record")
eBtn.grid(row=10, column=3)
eBtn.bind("<<Buttom-1>>", getSum)


lbLab = ttk.Label(page1, text="Select Patient")
lbLab.grid(column=3, row=2, columnspan=3, padx=150)
lb = Listbox(page1)
lb.grid(column=3, row=3, columnspan=3)

flist = os.listdir(rec_dir)

for item in flist:
        lb.insert(END, item)

def fileSelect(event):
    x = lb.curselection()[0]
    file = lb.get(x)
    path = f'{rec_dir}{file}'
    recOpen(path)

def recOpen(path):
    with open(path) as f:
        for line in f:
            sObj = Patient.from_string(line) #find better way of ending at last line
            loadNew(sObj)

lb.bind("<<ListboxSelect>>", fileSelect)

def loadNew(Patient):
    fnVal.config(text=Patient.fname)
    lnVal.config(text=Patient.lname)
    gVal.config(text=Patient.gender)
    aVal.config(text=Patient.age)
    idVal.config(text=Patient.paID)
    heightvalue.config(text=Patient.height)
    weightvalue.config(text=Patient.weight)
    tempvalue.config(text=Patient.btemp)
    sysvalue.config(text=Patient.s_bp)
    diavalue.config(text=Patient.d_bp) 
    pulsevalue.config(text=Patient.pulse)

nb.add(page1, text='View Patient Data')
nb.add(page2, text='Patient Visit Collection')

#nb.add(page2, text='View Insights')

nb.pack(expand=1, fill="both")

root.mainloop()

#if __name__ == "__main__":
    #demo()
