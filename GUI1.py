import tkinter as tk
def write_slogan():
    print("HELLO WORLD!!")

demolabel ="THIS IS A GUI ASSIGNMENT"
def demo_label(label):
    label.config(text=str(demolabel))


root = tk.Tk()
root.title("GUI Asignment 1")
root.geometry("400x400")
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="QUIT",fg="red",bg='black',command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,text="Hello",bg='blue',fg='black',command=write_slogan)
slogan.pack(side=tk.LEFT)

label = tk.Label(root, fg="dark green")
label.pack()
demo_label(label)


from tkinter import *

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.mainloop()