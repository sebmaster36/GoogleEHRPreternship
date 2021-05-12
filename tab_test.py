#!usr/bin/env python3

from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from patient import Patient
import os

dir_name = 'records'

def getvals():
    print(f"Updating Record for patient, {lnamevalue.get()}, {fnamevalue.get()}, ID: {IDvalue.get()}...")
    print("Updating Record for patient")

    #print(f"{fnamevalue.get(), lnamevalue.get(), gendervalue.get(), agevalue.get(), IDvalue.get(), heightvalue.get(), weightvalue.get(), tempvalue.get(), sysvalue.get(), diavalue.get(), pulsevalue.get()} ")

    with open(f"records/records_{IDvalue.get()}.txt", "a") as f:
        f.write(f"{IDvalue.get()},{fnamevalue.get()},{lnamevalue.get()},{agevalue.get()},{gendervalue.get()},{heightvalue.get()},{weightvalue.get()},{tempvalue.get()},{sysvalue.get()},{diavalue.get()},{pulsevalue.get()}\n")
        


#def demo():
root = tk.Tk()
root.title("Preternship Mock EMR")
root.geometry("600x700")
nb = ttk.Notebook(root)

# adding Frames as pages for the ttk.Notebook
# first page, which would get widgets gridded into it
page1 = ttk.Frame(nb)

height = ttk.Label(page1, text="Height (cm)").grid(column = 0, row = 0, padx = 30, pady = 15)
weight = ttk.Label(page1, text="Weight (kg)").grid(column = 0, row = 1, padx = 30, pady = 15)
temp = ttk.Label(page1, text="Body Temperature (Celsius)").grid(column = 0, row = 2, padx = 30, pady = 15)
sys = ttk.Label(page1, text="Systolic BP").grid(column = 0, row = 3, padx = 30, pady = 15)
dia = ttk.Label(page1, text="Diastolic BP").grid(column = 0, row = 4, padx = 30, pady = 15)
pulse = ttk.Label(page1, text="Pulse (BPM)").grid(column = 0, row = 5, padx = 30, pady = 15)

# Tkinter variable for storing entries
fnamevalue = StringVar()
lnamevalue = StringVar()
gendervalue = StringVar()
agevalue = IntVar()
IDvalue = IntVar()
heightvalue = IntVar()
weightvalue = IntVar()
tempvalue = DoubleVar()
sysvalue = IntVar()
diavalue = IntVar()
pulsevalue = IntVar()

heightentry = ttk.Entry(page1, textvariable=heightvalue).grid(column = 1, row = 0, padx = 30, pady = 15)
weightentry = ttk.Entry(page1, textvariable=weightvalue).grid(column = 1, row = 1, padx = 30, pady = 15)
tempentry = ttk.Entry(page1, textvariable=tempvalue).grid(column = 1, row = 2, padx = 30, pady = 15)
sysentry = ttk.Entry(page1, textvariable=sysvalue).grid(column = 1, row = 3, padx = 30, pady = 15)
diaentry = ttk.Entry(page1, textvariable=diavalue).grid(column = 1, row = 4, padx = 30, pady = 15)
pulseentry = ttk.Entry(page1, textvariable=pulsevalue).grid(column = 1, row = 5, padx = 30, pady = 15)

#Button to push input to file
btn = ttk.Button(text="Submit", command=getvals)
btn.pack(side = tk.BOTTOM)









# second page
page2 = ttk.Frame(nb)
text = ScrolledText(page2)
text.pack(expand=1, fill="both")

'''
# third page
page3 = ttk.Frame(nb)
text = ScrolledText(page3)
text.pack(expand=1, fill="both")
'''

nb.add(page1, text='Patient Visit Collection')


nb.pack(expand=1, fill="both")

root.mainloop()

#if __name__ == "__main__":
    #demo()
