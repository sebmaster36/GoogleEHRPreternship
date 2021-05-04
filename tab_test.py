#!usr/bin/env python3

from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def demo():
    root = tk.Tk()
    root.title("EMR")
    root.geometry("600x625")
    nb = ttk.Notebook(root)
    

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb)
    fname = ttk.Label(page1, text="First Name").grid(column = 0, row = 0, padx = 30, pady = 15)
    lname = ttk.Label(page1, text="Last Name").grid(column = 0, row = 1, padx = 30, pady = 15)
    gender = ttk.Label(page1, text="Gender").grid(column = 0, row = 2, padx = 30, pady = 15)
    age = ttk.Label(page1, text="Age").grid(column = 0, row = 3, padx = 30, pady = 15)
    ID = ttk.Label(page1, text="Patient ID").grid(column = 0, row = 4, padx = 30, pady = 15)
    height = ttk.Label(page1, text="Height").grid(column = 0, row = 5, padx = 30, pady = 15)
    weight = ttk.Label(page1, text="Weight").grid(column = 0, row = 6, padx = 30, pady = 15)
    temp = ttk.Label(page1, text="Body Temperature").grid(column = 0, row = 7, padx = 30, pady = 15)
    sys = ttk.Label(page1, text="Systolic").grid(column = 0, row = 8, padx = 30, pady = 15)
    dia = ttk.Label(page1, text="Diastolic").grid(column = 0, row = 9, padx = 30, pady = 15)
    pulse = ttk.Label(page1, text="Pulse").grid(column = 0, row = 10, padx = 30, pady = 15)
    
    fname = ttk.Entry(page1).grid(column = 1, row = 0, padx = 30, pady = 15)
    lname = ttk.Entry(page1).grid(column = 1, row = 1, padx = 30, pady = 15)
    gender = ttk.Entry(page1).grid(column = 1, row = 2, padx = 30, pady = 15)
    age = ttk.Entry(page1).grid(column = 1, row = 3, padx = 30, pady = 15)
    ID = ttk.Entry(page1).grid(column = 1, row = 4, padx = 30, pady = 15)
    height = ttk.Entry(page1).grid(column = 1, row = 5, padx = 30, pady = 15)
    weight = ttk.Entry(page1).grid(column = 1, row = 6, padx = 30, pady = 15)
    temp = ttk.Entry(page1).grid(column = 1, row = 7, padx = 30, pady = 15)
    sys = ttk.Entry(page1).grid(column = 1, row = 8, padx = 30, pady = 15)
    dia = ttk.Entry(page1).grid(column = 1, row = 9, padx = 30, pady = 15)
    pulse = ttk.Entry(page1).grid(column = 1, row = 10, padx = 30, pady = 15)




    # second page
    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    text.pack(expand=1, fill="both")

    # third page
    page3 = ttk.Frame(nb)
    text = ScrolledText(page3)
    text.pack(expand=1, fill="both")
   
    nb.add(page1, text='Data Collection')
    nb.add(page2, text='Summary')
    nb.add(page3, text='Visualizations')

    nb.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    demo()
