import pyautogui
from tkinter import *
import tkinter.ttk as ttk
from functools import partial



root = Tk()
root.geometry('640x480')
root.title('NIST File Downloader')

TCNLabel = Label(root, text="TCN Number")
TCNLabel.pack()
TCN_num = StringVar()
TCN_entry = Entry(root, textvariable=TCN_num)
TCN_entry.pack()
TCN = ["Inbox", "Submission", "Reply"]
typeLabel = Label(root, text="TCN Type")
typeLabel.pack()
TCN_type = ttk.Combobox(root, height=3, values=TCN, state="readonly")
TCN_type.current(0)
TCN_type.pack()


def getNIST():
    print(TCN_entry.get(), TCN_type.get())
submitButton = Button(root, text='Submit', command=getNIST)
submitButton.pack()


root.mainloop()
