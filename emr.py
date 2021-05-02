#!/usr/bin/env python3

from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")

    print(f"{fnamevalue.get(), lnamevalue.get(), gendervalue.get(), agevalue.get(), IDvalue.get(), heightvalue.get(), weightvalue.get(), tempvalue.get(), sysvalue.get(), diavalue.get(), pulsevalue.get()} ")



    with open(f"records_{IDvalue.get()}.txt", "a") as f:
        f.write(f"{fnamevalue.get(), lnamevalue.get(), gendervalue.get(), agevalue.get(), IDvalue.get(), heightvalue.get(), weightvalue.get(), tempvalue.get(), sysvalue.get(), diavalue.get(), pulsevalue.get()}\n ")

root.geometry("600x500")
#Heading
Label(root, text="EMR", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
fname = Label(root, text="First Name")
lname = Label(root, text="Last Name")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
ID = Label(root, text="Patient ID")
height = Label(root, text="Height")
weight = Label(root, text ="Weight")
temp = Label(root, text = "Body Temperature")
sys = Label(root, text = "Systolic")
dia = Label(root, text = "Diastolic")
pulse = Label(root, text = "Pulse")

#Pack text for our form
fname.grid(row=1, column=2)
lname.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
ID.grid(row=5, column=2)
height.grid(row=6, column=2)
weight.grid(row=7, column=2)
temp.grid(row=8, column=2)
sys.grid(row=9, column=2)
dia.grid(row=10, column=2)
pulse.grid(row=11, column=2)

# Tkinter variable for storing entries
fnamevalue = StringVar()
lnamevalue = StringVar()
#gendervalue = StringVar()
gendervalue = StringVar(root)
agevalue = IntVar()
IDvalue = IntVar()
heightvalue = IntVar()
weightvalue = IntVar()
tempvalue = IntVar()
sysvalue = IntVar()
diavalue = IntVar()
pulsevalue = IntVar()

#Entries for our form
fnameentry = Entry(root, textvariable=fnamevalue)
lnameentry = Entry(root, textvariable=lnamevalue)
genderentry = Entry(root, textvariable=gendervalue)
ageentry = Entry(root, textvariable=agevalue)
IDentry = Entry(root, textvariable=IDvalue)
heightentry = Entry(root, textvariable=heightvalue)
weightentry = Entry(root, textvariable=weightvalue)
tempentry = Entry(root, textvariable=tempvalue)
sysentry = Entry(root, textvariable=sysvalue)
diaentry = Entry(root, textvariable=diavalue)
pulseentry = Entry(root, textvariable=pulsevalue)

choices = {'Male', 'Female', 'N/A'}
gendervalue.set('Female')
popupMenu = OptionMenu(genderentry, *choices)
popupMenu.grid(row=3, column=3)

# Packing the Entries
fnameentry.grid(row=1, column=3)
lnameentry.grid(row=2, column=3)
#genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
IDentry.grid(row=5, column=3)
heightentry.grid(row=6, column=3)
weightentry.grid(row=7, column=3)
tempentry.grid(row=8, column=3)
sysentry.grid(row=9, column=3)
diaentry.grid(row=10, column=3)
pulseentry.grid(row=11, column=3)

#Checkbox & Packing it
#foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
#foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit", command=getvals).grid(row=12, column=3)

root.mainloop()
